import json

def recognize_customer(phone_number: str = "") -> dict:
    """
    Queries the caller database by phone number to verify the customer.
    Provides a robust fallback for GECX Cloud Simulator runs.
    """
    try:
        # Mock Customer Database matching PRD Scenarios
        MOCK_DATABASE = {
            "+31612345678": {
                "customer_id": "CZ-98765",
                "first_name": "Jan",
                "last_name": "de Jong",
                "account_status": "Active",
                "segment": "Gold Premium Telecom"
            },
            "+31687654321": {
                "customer_id": "CZ-44321",
                "first_name": "Sarah",
                "last_name": "Jenkins",
                "account_status": "Active",
                "segment": "Standard Broadband Only"
            },
            "+31611112222": {
                "customer_id": "CZ-12345",
                "first_name": "Mark",
                "last_name": "Evans",
                "account_status": "Active",
                "segment": "Standard Multi-Service"
            }
        }

        print(f"GECX Tool [recognize_customer]: phone_number: '{phone_number}'")
        cleaned_phone = str(phone_number).strip()

        # Self-Healing Fallback for Simulator runs
        if not cleaned_phone or cleaned_phone.lower() in ["", "unknown", "none", "null"]:
            profile = {
                "customer_id": "GUEST-00000",
                "first_name": "Guest",
                "last_name": "Visitor",
                "account_status": "Unverified",
                "segment": "Guest Account"
            }
        elif cleaned_phone in MOCK_DATABASE:
            profile = MOCK_DATABASE[cleaned_phone]
        else:
            profile = {
                "customer_id": "GUEST-00000",
                "first_name": "Guest",
                "last_name": "Visitor",
                "account_status": "Unverified",
                "segment": "Guest Account"
            }

        # Save to session variables
        context.state["recognised_customer"] = json.dumps(profile)
        return profile

    except Exception as e:
        print(f"[ERROR] recognize_customer failed: {e}")
        # Crucial Fix: Distinct error return path satisfying T001 linter rules!
        return {
            "customer_id": "GUEST-00000",
            "first_name": "Guest",
            "last_name": "Visitor",
            "account_status": "Unverified",
            "agent_action": "Tell the LLM that caller ID lookup failed, welcome them as a Guest, and politely request their name."
        }
