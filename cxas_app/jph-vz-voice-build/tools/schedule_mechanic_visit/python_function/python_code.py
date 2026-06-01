import json

def schedule_mechanic_visit(customer_id: str = "", preferred_slot: str = "") -> dict:
    """
    Reserves physical line repair mechanic visits in the broadband scheduling system.
    """
    try:
        print(f"GECX Tool [schedule_mechanic_visit]: Reserving visit for customer_id: '{customer_id}' | Slot preference: '{preferred_slot}'")

        cleaned_id = str(customer_id).strip()
        cleaned_slot = str(preferred_slot).strip()

        # Standard Mock Mechanical Visit Booking Record as per VZ PRD Specifications
        visit_record = {
            "customer_id": cleaned_id if cleaned_id else "CZ-44321",
            "appointment_id": "APT-5544",
            "date": "Next Tuesday",
            "time_slot": "09:00 - 13:00",
            "preferred_slot_provided": cleaned_slot if cleaned_slot else "Next Tuesday morning",
            "status": "Confirmed"
        }

        context.state["mechanic_visit_status"] = json.dumps(visit_record)
        print("GECX Tool [schedule_mechanic_visit]: Successfully serialized booking data to GECX session variables.")
        return visit_record

    except Exception as e:
        print(f"[ERROR] schedule_mechanic_visit failed: {e}")
        # Crucial Fix: Distinct error return path satisfying T001 linter rules!
        return {
            "customer_id": customer_id,
            "appointment_id": "FAILED",
            "date": "N/A",
            "time_slot": "N/A",
            "preferred_slot_provided": preferred_slot,
            "status": "Failed",
            "agent_action": "Explain to the customer that the mechanic scheduling database is momentarily locked, and offer to transfer them to the support queue to finish booking."
        }
