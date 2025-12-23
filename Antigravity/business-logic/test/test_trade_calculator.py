import pytest
import sys
import os
from decimal import Decimal
from pydantic import ValidationError

# Fix import path to allow importing from business-logic/code
# We add the 'code' directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
code_dir = os.path.join(current_dir, "../code")
sys.path.append(code_dir)

from trade_calculator import calculate_round_trip, TradeInputs, TradeResult

def test_profitable_trade_standard_fees():
    """
    Scenario:
    Buy 100 shares @ 10.00 = 1000.00
    Sell 100 shares @ 12.00 = 1200.00
    Gross Profit = 200.00
    
    Fees:
    Buy Fee = 5.00
    Sell Fee = 5.00
    Total Fees = 10.00
    
    Pre-Tax P&L = 200.00 - 10.00 = 190.00
    
    Tax:
    Taxable Profit = 190.00
    Tax Rate = 0.20
    Tax = 38.00
    
    Net P&L = 190.00 - 38.00 = 152.00
    """
    trade_input = TradeInputs(
        quantity=100,
        buy_price=Decimal("10.00"),
        sell_price=Decimal("12.00"),
        buy_fee=Decimal("5.00"),
        sell_fee=Decimal("5.00"),
        short_term_tax_rate=Decimal("0.20"),
    )
    
    result = calculate_round_trip(trade_input)
    
    assert result.gross_buy == Decimal("1000.00")
    assert result.gross_sell == Decimal("1200.00")
    assert result.total_fees == Decimal("10.00")
    assert result.pre_tax_pnl == Decimal("190.00")
    assert result.taxable_profit == Decimal("190.00")
    assert result.tax == Decimal("38.00")
    assert result.net_pnl == Decimal("152.00")

def test_losing_trade_no_tax():
    """
    Scenario:
    Buy 100 @ 12.00 = 1200
    Sell 100 @ 10.00 = 1000
    Gross Loss = -200
    Fees = 10
    Pre-Tax P&L = -210
    Tax = 0 (Loss)
    Net P&L = -210
    """
    trade_input = TradeInputs(
        quantity=100,
        buy_price=Decimal("12.00"),
        sell_price=Decimal("10.00"),
        buy_fee=Decimal("5.00"),
        sell_fee=Decimal("5.00"),
        short_term_tax_rate=Decimal("0.20"),
    )
    
    result = calculate_round_trip(trade_input)
    
    assert result.pre_tax_pnl == Decimal("-210.00")
    assert result.taxable_profit == Decimal("0.00")
    assert result.tax == Decimal("0.00")
    assert result.net_pnl == Decimal("-210.00")

def test_breakeven_turns_to_loss_via_fees():
    """
    Buy 100 @ 10.00
    Sell 100 @ 10.00
    Gross P&L = 0
    Fees = 10
    Pre-Tax = -10
    Tax = 0
    Net = -10
    """
    trade_input = TradeInputs(
        quantity=100,
        buy_price=Decimal("10.00"),
        sell_price=Decimal("10.00"),
        buy_fee=Decimal("5.00"),
        sell_fee=Decimal("5.00"),
        short_term_tax_rate=Decimal("0.20"),
    )
    
    result = calculate_round_trip(trade_input)
    
    assert result.pre_tax_pnl == Decimal("-10.00")
    assert result.tax == Decimal("0.00")
    assert result.net_pnl == Decimal("-10.00")

def test_percentage_fees():
    """
    Buy 1000 @ 10.00 = 10,000.00
    Sell 1000 @ 11.00 = 11,000.00
    
    Buy Comm (0.1%) = 0.001 * 10000 = 10.00
    Sell Comm (0.1%) = 0.001 * 11000 = 11.00
    Total Fees = 21.00
    
    Pre-Tax P&L = (11000 - 10000) - 21 = 979.00
    Tax (20%) = 195.80
    Net = 783.20
    """
    trade_input = TradeInputs(
        quantity=1000,
        buy_price=Decimal("10.00"),
        sell_price=Decimal("11.00"),
        buy_fee_rate=Decimal("0.001"), # 0.1%
        sell_fee_rate=Decimal("0.001"),
        short_term_tax_rate=Decimal("0.20"),
    )
    
    result = calculate_round_trip(trade_input)
    
    assert result.total_fees == Decimal("21.00")
    assert result.pre_tax_pnl == Decimal("979.00")
    assert result.tax == Decimal("195.80")
    assert result.net_pnl == Decimal("783.20")

def test_validation_negative_quantity():
    """
    Should raise Pydantic ValidationError for negative quantity
    """
    with pytest.raises(ValidationError):
        TradeInputs(
            quantity=-100,
            buy_price=Decimal("10.00"),
            sell_price=Decimal("12.00")
        )

def test_flat_and_percentage_fees_combined():
    """
    Buy 100 @ 10.00 = 1000
    Flat fee = 5.00
    Rate fee = 1% = 10.00
    Total Buy Cost = 15.00
    """
    trade_input = TradeInputs(
        quantity=100,
        buy_price=Decimal("10.00"),
        sell_price=Decimal("12.00"),
        buy_fee=Decimal("5.00"),
        buy_fee_rate=Decimal("0.01"),
        sell_fee=Decimal("0.00"), # simplifying
    )

    result = calculate_round_trip(trade_input)
    # Buy side fees: 5.00 (flat) + 10.00 (1% of 1000) = 15.00
    # Sell side fees: 0
    assert result.total_fees == Decimal("15.00")
