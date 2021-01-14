---
sidebarDepth: 2
editLink: false
---
# run
---
<h3>flow</h3>
  Run a flow that is registered to the Prefect API

  <pre><code>Options:<br>      --name, -n                  TEXT        The name of a flow to run [required]<br>      --project, -p               TEXT        The name of a project that contains<br>                                              the flow [required]<br>      --version, -v               INTEGER     A flow version to run<br>      --parameters-file, -pf      FILE PATH   A filepath of a JSON file containing<br>                                              parameters<br>      --parameters-string, -ps    TEXT        A string of JSON parameters (note: to ensure these are<br>                                              parsed correctly, it is best to include the full payload<br>                                              within single quotes)<br>      --run-name, -rn             TEXT        A name to assign for this run<br>      --context, -c               TEXT        A string of JSON key / value pairs to include in context<br>                                              (note: to ensure these are parsed correctly, it is best<br>                                              to include the full payload within single quotes)<br>      --watch, -w                             Watch current state of the flow run, stream<br>                                              output to stdout<br>      --logs, -l                              Get logs of the flow run, stream output to<br>                                              stdout<br>      --no-url                                Only output the flow run id instead of a<br>                                              link<br><br>  If both `--parameters-file` and `--parameters-string` are provided then the values<br>  passed in through the string will override the values provided from the file.<br><br>  e.g.<br>  File contains:  {"a": 1, "b": 2}<br>  String:         '{"a": 3}'<br>  Parameters passed to the flow run: {"a": 3, "b": 2}<br><br>  Example:<br>      $ prefect run flow -n "Test-Flow" -p "My Project" -ps '{"my_param": 42}'<br>      Flow Run: https://cloud.prefect.io/myslug/flow-run/2ba3rrfd-411c-4d99-bb2a-f64a6dea78f9<br><br></code></pre>
<p class="auto-gen">This documentation was auto-generated from commit <a href='https://github.com/PrefectHQ/prefect/commit/n/a'>n/a</a> </br>on December 16, 2020 at 21:36 UTC</p>