Issue:
Report endpoints authenticated the user but did not verify report ownership.

Why it matters:
A user could access another user's report, score, or modify their readings by
changing the report_id.

Fix:
Added get_owned_report() and used it in all report-specific endpoints.



Issue:
Missing biomarkers were treated as a value of 0 and included in the pillar
average.

Why it matters:
An unmeasured biomarker could incorrectly reduce a patient's health score.

Fix:
Missing markers are now skipped and only supplied measurements contribute to
the pillar average.


Issue:
Skipping missing markers could leave a pillar with zero measurements and cause
a division-by-zero error.

Why it matters:
A report containing only some biomarkers could cause the scoring endpoint to
fail.

Fix:
Pillars with no measurements now receive 0 points instead of causing an error.




Issue:
The login endpoint returned the user's password in the response.

Why it matters:
Returning credentials exposes sensitive authentication information to clients
and potentially to logs or other systems handling the response.

Fix:
Removed the password from the login response and added a regression test.