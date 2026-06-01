import json

def escalate_to_human(customer_id: str = "", context_summary: str = "") -> dict:
    """
    Initiates a context-preserving warm transfer to live support advisor queues.
    Dynamically routes to either Technical Support or Account Administration based on context.
    """
    try:
        print(f"GECX Tool [escalate_to_human]: Compiling escalation context for customer_id: '{customer_id}'")
        print(f"GECX Tool [escalate_to_human]: Context summary payload received:\n  '{context_summary}'")

        cleaned_id = str(customer_id).strip()
        cleaned_summary = str(context_summary).strip()

        # Determine routing queue based on contextual keyword evaluation
        summary_lower = cleaned_summary.lower()
        if any(keyword in summary_lower for keyword in ["wifi", "outage", "modem", "telemetry", "packet", "diagnose"]):
            target_queue = "Technical_Level_2_Support"
        else:
            target_queue = "Account_Administration"

        # Standard Mock Handoff Record as per VZ PRD Specifications
        transfer_record = {
            "customer_id": cleaned_id if cleaned_id else "CZ-44321",
            "transfer_status": "Success",
            "target_queue": target_queue,
            "context_summary_payload": cleaned_summary
        }

        context.state["escalation_context"] = json.dumps(transfer_record)
        print(f"GECX Tool [escalate_to_human]: Successfully packaged context and routed to live queue: '{target_queue}'")
        return transfer_record

    except Exception as e:
        print(f"[ERROR] escalate_to_human failed: {e}")
        # Crucial Fix: Distinct error return path satisfying T001 linter rules!
        return {
            "customer_id": customer_id,
            "transfer_status": "Failed",
            "target_queue": "General_Advisor_Queue",
            "agent_action": "Apologize to the customer that the automated warm transfer system encountered a glitch, and perform a direct general team transfer instead."
        }
