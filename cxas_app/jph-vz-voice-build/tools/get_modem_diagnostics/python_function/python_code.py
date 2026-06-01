import json

def get_modem_diagnostics(customer_id: str = "") -> dict:
    """
    Audits raw modem telemetry parameters and local area outages.
    """
    try:
        print(f"GECX Tool [get_modem_diagnostics]: Triggering real-time network audit for customer_id: '{customer_id}'")

        cleaned_id = str(customer_id).strip()

        # Standard Mock Telemetry Diagnostics Record as per VZ PRD Specifications
        telemetry_record = {
            "customer_id": cleaned_id if cleaned_id else "CZ-44321",
            "modem_id": "MOD-8812",
            "status": "Online",
            "signal_strength": "Weak",
            "packet_loss": "High",
            "area_outage": False
        }

        context.state["telemetry_diagnostics"] = json.dumps(telemetry_record)
        print("GECX Tool [get_modem_diagnostics]: Successfully serialized network diagnostic telemetry to GECX session variables.")
        return telemetry_record

    except Exception as e:
        print(f"[ERROR] get_modem_diagnostics failed: {e}")
        # Crucial Fix: Distinct error return path satisfying T001 linter rules!
        return {
            "customer_id": customer_id,
            "modem_id": "UNKNOWN",
            "status": "Offline",
            "signal_strength": "None",
            "packet_loss": "N/A",
            "area_outage": False,
            "agent_action": "Inform the customer that the automated network diagnostic server is currently unresponsive, apologize for the inconvenience, and offer to escalate to a level 2 technician."
        }
