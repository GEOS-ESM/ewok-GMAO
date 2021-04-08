# ewok-GMAO
Ewok for GMAO

This repository assumes that ewok, r2d2, and solo were successfully built and a local ewok environment has been created. Also, please make sure to source the ewok modules.

## Installation
To run, make sure that copy_tasks.sh, external_ew_create_experiment, and external_ewok_create_experiment are executable by running the following command:

```chmod +x  copy_tasks.sh external_ew*```

Set the environmental variable EWOK_ENV to your current ewok environment:

Example:

(Bash)
```EWOK_ENV=/discover/nobackup/$USER/JediEwok/opt/ewok-env/```

(Cshell)
```setenv EWOK_ENV /discover/nobackup/$USER/JediEwok/opt/ewok-env/```

Run copy_tasks.sh using the following command:

```./copy_tasks.sh```

This copies all tasks from the tasks directory to the ewok environment directory that the suites link to. 
**Note that you would have to run this task again whenever you rebuild ewok or whenever you create a new task.**

To create an experiment, run the following command:

```./external_ewok_create_experiment tutorial_hello.yaml -p $EwokPort```

where $EwokPort is whatever port you have set. 
