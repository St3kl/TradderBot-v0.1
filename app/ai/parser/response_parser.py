def parse_response(response):
    """
    Cleans and validates the LLM response.
    """

    if response is None:
        return "No AI response."

    response = response.strip()

    if response == "":
        return "Empty AI response."

    return response