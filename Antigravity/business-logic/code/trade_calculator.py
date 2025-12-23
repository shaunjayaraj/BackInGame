from decimal import Decimal, ROUND_HALF_UP
from pydantic import BaseModel, Field, field_validator
from typing import Optional

# Set context for all Decimal operations to ensure consistency if needed
# For now, we rely on Decimal's default context but enforce rounding implicitly where needed.

class TradeInputs(BaseModel):
    quantity: int = Field(..., gt=0, description="Number of shares bought and sold")
    buy_price: Decimal = Field(..., ge=0, description="Price per share at buy")
    sell_price: Decimal = Field(..., ge=0, description="Price per share at sell")
    
    # Fees - Flat
    buy_fee: Decimal = Field(default=Decimal("0.00"), ge=0, description="Flat fee for buy leg")
    sell_fee: Decimal = Field(default=Decimal("0.00"), ge=0, description="Flat fee for sell leg")
    
    # Fees - Rates (percentages like 0.001 for 0.1%)
    buy_fee_rate: Decimal = Field(default=Decimal("0.00"), ge=0, description="Fee rate for buy leg")
    sell_fee_rate: Decimal = Field(default=Decimal("0.00"), ge=0, description="Fee rate for sell leg")
    
    # Tax
    short_term_tax_rate: Decimal = Field(default=Decimal("0.00"), ge=0, le=1, description="Tax rate on profit")

    @field_validator("buy_price", "sell_price", "buy_fee", "sell_fee", "buy_fee_rate", "sell_fee_rate", "short_term_tax_rate", mode="before")
    def parse_decimal_if_needed(cls, v):
        """Allow passing strings or floats/ints, converting to Decimal automatically."""
        if v is None:
            return Decimal("0.00")
        return Decimal(str(v))

class TradeResult(BaseModel):
    gross_buy: Decimal
    gross_sell: Decimal
    total_fees: Decimal
    pre_tax_pnl: Decimal
    taxable_profit: Decimal
    tax: Decimal
    net_pnl: Decimal

def calculate_round_trip(inputs: TradeInputs) -> TradeResult:
    # 1. Gross Amounts
    gross_buy = inputs.quantity * inputs.buy_price
    gross_sell = inputs.quantity * inputs.sell_price
    
    # 2. Fees
    # Commission = Notional * Rate
    buy_commission = gross_buy * inputs.buy_fee_rate
    sell_commission = gross_sell * inputs.sell_fee_rate
    
    # Total per leg
    total_buy_fees = inputs.buy_fee + buy_commission
    total_sell_fees = inputs.sell_fee + sell_commission
    
    total_fees = total_buy_fees + total_sell_fees
    
    # 3. Pre-Tax P&L
    # (Sell - Buy) - Fees
    gross_pnl = gross_sell - gross_buy
    pre_tax_pnl = gross_pnl - total_fees
    
    # 4. Taxable Amount
    # Only profit is taxed.
    if pre_tax_pnl > Decimal("0"):
        taxable_profit = pre_tax_pnl
    else:
        taxable_profit = Decimal("0")
        
    # 5. Tax
    tax = taxable_profit * inputs.short_term_tax_rate
    
    # 6. Net P&L
    net_pnl = pre_tax_pnl - tax
    
    # Rounding Policy
    # In finance, typically round to 2 decimal places at the very end for display,
    # or at specific "payment" boundaries. Here we round the final output fields.
    # Standard: Round Half Up (Banker's rounding is ROUND_HALF_EVEN, standard commercial is often HALF_UP)
    # The user asked for "Decimal (and a fixed rounding policy)".
    # We will apply rounding to the result fields for consistency.
    
    def round_money(amount: Decimal) -> Decimal:
        return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    return TradeResult(
        gross_buy=round_money(gross_buy),
        gross_sell=round_money(gross_sell),
        total_fees=round_money(total_fees),
        pre_tax_pnl=round_money(pre_tax_pnl),
        taxable_profit=round_money(taxable_profit),
        tax=round_money(tax),
        net_pnl=round_money(net_pnl)
    )
