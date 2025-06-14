from valuation_tools import get_financials, run_valuation, check_rai_compliance

def entry_point(request):
    query = request.get("text", "").lower()

    if "snowflake" in query:
        company = "SNOW"
    elif "datadog" in query:
        company = "DDOG"
    else:
        return { "response": "Please ask about Snowflake or Datadog to evaluate." }

    financials = get_financials(company)
    valuation = run_valuation(financials)
    compliance = check_rai_compliance(financials)

    return {
        "response": f"📊 {company} Valuation Report:\n{valuation}\n{compliance}",
        "context": {"last_company": company}
    }