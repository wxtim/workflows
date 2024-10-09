# Rose Stem Example

A simple Rose Stem example.

This Rose Stem test workflow runs tests of foods. Depending on
the options it will try baking, frying, grilling or boiling them.

Try changing the ``--group`` settings.

## To install this workflow:

```bash

    rose stem \
        --source rose-stem-eg=$PWD \
        --workflow-name throwaway/rose-stem-eg \
        --group boil,bake   # fry,grill also available

    # What is the effect of different settings of --group?
    cylc config throwaway/rose-stem-eg
```

### Notes

n.b. ``rose-stem-eg=$PWD`` give the source a name. Without
giving the source a name rose stem will look for a name using
Subversion and will fail because this isn't a Subversion repo.

Without ``--workflow-name`` the workflow will be installed in
``~/cylc-run/rose-stem``. This may well fail if there's a different
Rose Stem workflow in that location.
"""

### Versions

written for cylc version = 8.x
tested with cylc version = 8.3.5.dev
