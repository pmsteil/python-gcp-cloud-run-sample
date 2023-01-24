# benchmarks.sh

# Example usage:
# ./benchmarks.sh (default 100 iterations, runs both parallel and sequential)
# ./benchmarks.sh 1000 1 (runs 1000 iterations, runs both parallel and sequential)
# ./benchmarks.sh 100 1 0 (runs 100 iterations, runs only parallel)
# ./benchmarks.sh 100 0 1 (runs 100 iterations, runs only sequential)

# if first argument is -h or --help, print usage
if [ "$1" = "local" ]; then
    baseuri=http://127.0.0.1:8080
elif [ "$1" = "remote" ]; then
    baseuri=https://docker-brandx-api-py-jflup3ylrq-wn.a.run.app
#elif [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
else
    clear
    echo "-------------------------------------------------------------"

    echo "Usage: ./benchmarks.sh [iterations] [parallel] [sequential]"
    echo "iterations: number of iterations to run (default 100)"
    echo "parallel: 1 to run parallel requests, 0 to skip (default 1)"
    echo "sequential: 1 to run sequential requests, 0 to skip (default 1)"
    echo 
    echo "Example usage:"
    echo "./benchmarks.sh (default 100 iterations, runs both parallel and sequential)"
    echo "./benchmarks.sh 1000 1 (runs 1000 iterations, runs both parallel and sequential)"
    echo "./benchmarks.sh 100 1 0 (runs 100 iterations, runs only parallel)"
    echo "./benchmarks.sh 100 0 1 (runs 100 iterations, runs only sequential)"    
    echo "-------------------------------------------------------------"

    exit 0
fi



# accept cli arg called local to set baseuri to localhost
# if [ "$1" = "local" ]; then
#     baseuri=http://127.0.0.1:8080
# fi

# if [ "$1" = "remote" ]; then
#     baseuri=https://docker-brandx-api-py-jflup3ylrq-wn.a.run.app
# fi

# if [ "$1" = "" ]; then
#     $1 = "-h"
# fi



# create array of uris to test
declare -a uris
uris[0]=$baseuri/
uris[1]=$baseuri/hello
uris[2]=$baseuri/pubSubProcessBCImport
# uris[3]=$baseuri/pubSubProcessMi9Import





# accept commandline arguments for iterations and default it to 10 if not provided
iterations=${2:-10}

# accept commandline arguments for parallel requests and default it to 1 if not provided
parallel=${3:-1}
sequential=${4:-1}


# echo "-------------------------------------------------------------"
# echo "Executing $iterations iterations"
# echo "Running parallel requests: $parallel"
# echo "Running sequential requests: $sequential"
# echo "-------------------------------------------------------------"

# loop over all uris in array and execute block if $parallel eq 1
if [ $parallel -eq 1 ]; then
    for uri in "${uris[@]}"
    do
        echo "-------------------------------------------------------------"
        echo "Running $iterations iterations of $uri in parallel"
        echo "-------------------------------------------------------------"
        #ab -n $iterations -c 10 $uri
        ab -n $iterations -c $iterations $uri
    done
fi

# loop over all uris in array and execute block if $sequential eq 1
if [ $sequential -eq 1 ]; then
    for uri in "${uris[@]}"
    do
        echo "-------------------------------------------------------------"
        echo "Running $iterations iterations of $uri sequentially"
        echo "-------------------------------------------------------------"
        # run it iterations times
        for i in $(seq 1 $iterations); do
            curl -s $uri
        done
    done
fi

# if [ $parallel -eq 1 ]; then
#     # run x requests in parallel
#     echo "Executing $iterations requests in parallel"
#     ab -n $iterations -c $iterations $uri
# fi

# if [ $sequential -eq 1 ]; then
#     # run x requests sequentially
#     for i in $(seq 1 $iterations); do  
#     curl -s $uri
#     done
# fi
