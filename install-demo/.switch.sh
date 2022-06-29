#!/bin/bash
if [[ -f suite.rc ]]; then
  mv suite.rc .suite.rc
  mv .flow.cylc flow.cylc
  find . -name "*.conf" -exec sed -i 's@jinja2:suite.rc@template variables@' {} \;
else
  mv .suite.rc suite.rc
  mv flow.cylc .flow.cylc
  find . -name "*.conf" -exec sed -i 's@template variables@jinja2:suite.rc@' {} \;
fi