import streamlit as st
import json, time, os

st.set_page_config(page_title="AyooX Nexus | Live Pulse", layout="wide")

def load_vitals():
    try:
        # Durable state reading from the live heartbeat log
        if os.path.exists("handshake.log"):
            with open("handshake.log", "r") as f:
                return json.load(f)
    except:
        pass
    return {"status": "CONNECTING...", "throughput": "0 GB/s"}

v = load_vitals()

st.title("🛡️ AyooX Nexus: Durable Pipeline Monitor")
st.subheader("Sovereign Identity: ayodeleomolabi@ayoox.com")

# Operational Evidence Metrics
c1, c2, c3 = st.columns(3)
c1.metric("Metabolic Throughput", v.get("throughput", "0 GB/s"), delta="LIVE")
c2.metric("Sentry Verification", v.get("status", "SEARCHING..."))
c3.metric("System Health", "DURABLE" if v.get("status") == "RSA_SIGN_VERIFIED" else "RETRYING")

# Metadata scar log (Observed Reality)
if "session_id" in v:
    st.info(f"Session Trace: {v['session_id']} | Load: {v.get('rate_limit_usage', '0%')}")

# Force live rerun every second for real-time observability
time.sleep(1)
st.rerun()
