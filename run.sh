#!/usr/bin/env bash

# check on number of arguments
if [ "$#" -ne 1 ]; then
    echo -e "Illegal number of parameters\nUsage:\n\t$0 --normal\nOR\n\t$0 --test"
    exit 1
fi

option=$1
if [ "$option" = "--normal" ]; then
    echo "Press <D> to stop."
    docker-compose up --build &
    while true; do
        echo "Press <D> to stop."
        for ((n = 0; n < 6; n++)); do
            sleep 1
            IFS= read -r -t 0.25 -n 1 -s holder && var="$holder"
            if [[ $var = "d" ]] || [[ $var = "D" ]]; then
                docker-compose down
                break 2
            fi
        done
    done
    exit 0
fi
if [ "$option" = "--test" ]; then
    echo "Press <D> to stop."
    docker-compose -f docker-compose-test.yml up --build &
    while true; do
        echo "Press <D> to stop."
        for ((n = 0; n < 6; n++)); do
            sleep 1
            IFS= read -r -t 0.25 -n 1 -s holder && var="$holder"
            if [[ $var = "d" ]] || [[ $var = "D" ]]; then
                docker-compose -f docker-compose-test.yml down
                break 2
            fi
        done
    done
    exit 0
fi
