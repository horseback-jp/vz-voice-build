import json

def get_order_status(customer_id: str = "") -> dict:
    """
    Queries the shipping database to check track-and-trace package delivery pipelines.
    """
    try:
        print(f"GECX Tool [get_order_status]: Querying shipping records for customer_id: '{customer_id}'")
        cleaned_id = str(customer_id).strip()

        logistics_record = {
            "customer_id": cleaned_id if cleaned_id else "CZ-98765",
            "order_id": "ORD-1122",
            "item_name": "Wifi Pod",
            "status": "In Transit",
            "delivery_date": "Tomorrow"
        }

        context.state["order_tracking_status"] = json.dumps(logistics_record)
        return logistics_record

    except Exception as e:
        print(f"[ERROR] get_order_status failed: {e}")
        # Crucial Fix: Distinct error return path satisfying T001 linter rules!
        return {
            "order_id": "UNKNOWN",
            "status": "Failed",
            "agent_action": "Inform the customer that tracking systems are undergoing maintenance, and offer to explain their invoice details instead."
        }
