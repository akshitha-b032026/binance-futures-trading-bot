import argparse

from bot.orders import place_order

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)

parser = argparse.ArgumentParser(
    description="Binance Futures Trading Bot"
)

parser.add_argument(
    "--symbol",
    required=True
)

parser.add_argument(
    "--side",
    required=True
)

parser.add_argument(
    "--type",
    required=True
)

parser.add_argument(
    "--quantity",
    required=True,
    type=float
)

parser.add_argument(
    "--price",
    type=float
)

args = parser.parse_args()

try:

    validate_side(args.side)

    validate_order_type(args.type)

    validate_quantity(args.quantity)

    if (
        args.type == "LIMIT"
        and args.price is None
    ):
        raise ValueError(
            "Price required for LIMIT order"
        )

    print("\n===== ORDER REQUEST =====")

    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")

    if args.price:
        print(f"Price: {args.price}")

    response = place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    print("\n===== ORDER RESPONSE =====")

    print(
        f"Order ID: {response.get('orderId')}"
    )

    print(
        f"Status: {response.get('status')}"
    )

    print(
        f"Executed Qty: {response.get('executedQty')}"
    )

    print("\nSUCCESS")

except Exception as e:

    print("\nFAILED")
    print(str(e))