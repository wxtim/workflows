### Data Retrieve & Process Workflow
Contains 2 tasks:

- data_getter: Does not need much memory, but requires a longer timeout limit.
  may need retrying.
- data_handler: Needs much more memory, and should only happen if the data
  getter suceeds.
- tell_me_what_resources_i_used: Optional 3rd task prints the computer cost
  of the first two tasks.

