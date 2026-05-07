

### **📂 Portfolio Project: Monthly Incident Insights & Trend Report**

**Report Title:** Monthly Operational Risk & Cybersecurity Incident Trend Summary

**Reporting Period:** April 2026

**Target Audience:** Operational Risk Committee (ORC)

**Regulatory Context:** APRA CPS 234 (Information Security) & ASD Essential Eight

---

#### **1. Executive Summary**

In April 2026, the bank's detection systems recorded a stabilization in general malware but a sharp, targeted spike in social engineering attacks. Total cybersecurity incidents remained within the "Amber" threshold; however, the emergence of a new phishing variant targeting the Finance Department represents a material threat to the bank's capital through potential Authorised Push Payment (APP) fraud.

---

#### **2. Technical Trend Analysis: The .lnk Phishing Spike**

* **The Trend:** We identified a **22% month-over-month increase** in phishing attempts using malicious `.lnk` (shortcut) file attachments.
* **Targeting:** 85% of these attempts specifically targeted users within the **Finance and Fraud Control** departments.
* **The Payload:** The `.lnk` files were designed to trigger a PowerShell reverse shell, bypassing traditional "Sandbox" scanners that only look for executable files (like `.exe`).

---

#### **3. Fraud Intersection: Authorised Push Payments (APP)**

* **Observation:** While technical "Card Theft" fraud is decreasing, **APP Scams** (where customers are coached to authorize a transaction) now account for **70% of confirmed losses**.
* **The Link:** Technical breaches in the Contact Centre or Finance team (via the `.lnk` spike) are often the "pre-cursor" to APP scams. Attackers seek internal credentials to gain "Insider Knowledge," making their calls to customers sound more legitimate.

---

#### **4. Causal Factor Analysis (The "Why")**

The root cause of this vulnerability is **Control Obsolescence**.

* **Legacy Email Filters:** Our current email gateway is configured to block active content in PDFs and Office docs but does not inspect the metadata of Windows Shortcut (`.lnk`) files.
* **Human Layer Failure:** Despite existing training, 3 members of the Finance team attempted to open the files, indicating that current "Generic" training is not sufficient for "High-Value" roles.

---

#### **5. Regulatory & Framework Mapping**

* **APRA CPS 234:** This incident represents a failure to maintain an "Information Security Capability" commensurate with the evolving threat landscape (Clause 13).
* **ASD Essential Eight (User Application Hardening):** We are currently at **Maturity Level 1**. The PowerShell execution by a non-technical user violates the requirement to restrict administrative and scripting tools.

---

#### **6. Proposed Uplift & Remediation**

| Proposed Action | Type | JD Match |
| --- | --- | --- |
| **GPO Update:** Implement PowerShell "Constrained Language Mode" for all non-IT staff. | Technical | *Identify causal factors* |
| **Email Gateway Tuning:** Update filters to quarantine all incoming shortcut files from external domains. | Technical | *Support remediation activities* |
| **Targeted Simulations:** Deploy a Finance-specific phishing simulation based on the "Invoice" template seen in April. | Managerial | *Support end-to-end RCSA* |
| **APP Transaction Friction:** Implement a 24-hour "cooling off" period for first-time high-value transfers initiated via mobile app. | Operational | *Contribute to resilience uplift* |
