def calculate_pnl(

    direction,

    entry,

    exit_price,

    position_size

):

    if direction == "LONG":

        return (

            exit_price - entry

        ) * position_size

    return (

        entry - exit_price

    ) * position_size