library("r2ddi")

dir2xml(
  path_in = "temp/v3-0-0/en/",
  path_out = "r2ddi/v3-0-0/en/",
  missing_codes=-99:-70, 
  my_cores=30)
