def get_financials(ticker):
    mock_data = {
        "SNOW": {"revenue": 2100000000, "pe_ratio": 37.5},
        "DDOG": {"revenue": 1800000000, "pe_ratio": 29.3}
    }
    return mock_data.get(ticker.upper(), {"revenue": 1000000000, "pe_ratio": 20.0})

def run_valuation(financials):
    valuation = financials["revenue"] * 8
    return f"Valuation estimate: ${valuation / 1e9:.2f}B"

def check_rai_compliance(financials):
    if financials["pe_ratio"] > 35:
        return "Attention: High P/E ratio may indicate RAI risk. Review recommended."
    return "Compliant with risk standards."