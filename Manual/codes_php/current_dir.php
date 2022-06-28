$currentDirectoryName = basename(__DIR__);
echo 'Currently in the '.$currentDirectoryName .' directory <br><br>';

$fullPath = dir(getcwd());
echo 'The full path is: ' . $fullPath->path . '<br>';
