### Running on SPICE
        A template for submission of jobs to a SPICE cluster.

        ### Warning
        > This suite submits very small jobs to a SPICE cluster if you site has one
        > set up.
        >
        > Jobs this size are NOT a good use of SPICE resources. Use of this suite
        > for purposes other than learning may bring unwanted attention from your
        > system admins.

        ### How to find out about your jobs SPICE resource usage.

        Look at the output of the tell_me_what_resources_i_used task at
        ~/cylc-run/spice_simplest/log/job/<final cycle point>/tell_me_what_resources_i_used/NN/job.out

        Run this script in a different terminal to see what SPICE is doing:
        ```
        now=$(date +%H:%M)
        export SACCT_FORMAT=
