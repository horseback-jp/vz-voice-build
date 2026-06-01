import json

def retrieve_invoice_data(customer_id: str = "") -> dict:
    """
    Queries the billing database to explain monthly bill variances.
    """
    try:
        print(f"GECX Tool [retrieve_invoice_data]: Querying invoices for customer_id: '{customer_id}'")
        cleaned_id = str(customer_id).strip()

        billing_record = {
            "customer_id": cleaned_id if cleaned_id else "CZ-98765",
            "current_bill": 75.00,
            "previous_bill": 60.00,
            "currency": "EUR",
            "itemized_charges": [
                {
                    "item": "Wifi Pod (Monthly fee)",
                    "cost": 15.00,
                    "category": "Hardware Deal Addition"
                }
            ]
        }

        context.state["billing_variance"] = json.dumps(billing_record)
        return billing_record

    except Exception as e:
        print(f"[ERROR] retrieve_invoice_data failed: {e}")
        # Crucial Fix: Distinct error return path satisfying T001 linter rules!
        return {
            "current_bill": 0.00,
            "previous_bill": 0.00,
            "itemized_charges": [],
            "agent_action": "Inform the customer that the billing system is temporarily offline, and offer to transfer them to Account Administration."
        }
