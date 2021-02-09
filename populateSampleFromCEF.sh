#!/bin/bash
while IFS= read -r line;do
    echo $line
    logger -p local4.warn -t CEF $line
done < "$1"