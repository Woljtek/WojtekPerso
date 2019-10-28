# Test a version  (with vboxmanage)
#!/bin/bash
currentver="$(vboxmanage --version | head -n1 | cut -d"r" -f1)"
requiredver="4.3.26"
 if [ "$(printf '%s\n' "$requiredver" "$currentver" | sort -V | head -n1)" = "$requiredver" ]; then
        echo "Greater than or equal to 5.0.0"
 else
        echo "Less than 5.0.0"
 fi
