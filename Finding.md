1.Issue:
Report endpoints authenticated the user but did not verify report ownership.

Why it matters:
A user could access another user's report, score, or modify their readings by
changing the report_id.

Fix:
Added get_owned_report() and used it in all report-specific endpoints.



2.Issue:
Missing biomarkers were treated as a value of 0 and included in the pillar
average.

Why it matters:
An unmeasured biomarker could incorrectly reduce a patient's health score.

Fix:
Missing markers are now skipped and only supplied measurements contribute to
the pillar average.


3.Issue:
Skipping missing markers could leave a pillar with zero measurements and cause
a division-by-zero error.

Why it matters:
A report containing only some biomarkers could cause the scoring endpoint to
fail.

Fix:
Pillars with no measurements now receive 0 points instead of causing an error.




4.Issue:
The login endpoint returned the user's password in the response.

Why it matters:
Returning credentials exposes sensitive authentication information to clients
and potentially to logs or other systems handling the response.

Fix:
Removed the password from the login response and added a regression test.



Normalization helper

I built the normalization helper around a small alias-to-canonical-name mapping. The MARKER_ALIASES dictionary maps lab-specific names such as FBS, A1c, and trigs to the canonical marker names expected by the scoring engine. I kept the normalization logic separate from the scoring logic so that the scoring engine continues to work only with canonical marker names.

The normalize_marker() function handles a single marker name, while normalize_readings() applies that logic to an entire readings dictionary. Known canonical names are preserved, known aliases are converted, and unknown marker names are ignored safely rather than being passed into the scoring engine. This keeps the helper small, explicit, and easy to extend when new lab aliases are added.

AI tool usage

I used AI tools during the task to help me understand the existing code, reason through the authorization and scoring issues, understand the normalization requirements, and review/debug my tests.