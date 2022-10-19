### Demonstrate using cylc play -t
        This workflow contains two workflows, animals and fungi
        which live largely separate existences.

        If the user plays them using cylc vip then both will
        be run, but the user can choose to use

        ```
        cylc vip -t 2612/start_animals
        cylc vip -t 2710/start_fungi
        ```

        To effectively run only one workflow.
    
