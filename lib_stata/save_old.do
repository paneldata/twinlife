clear
set more off

set maxvar 30000

* data/distribution version string (dvs)
local dvs "v3-0-0"  

* original data path
* local ori_data_path  "../../data/twinlife/v2_1/en"
* local ori_data_path "./DATA/`dvs'/en/"
local ori_data_path "./DATA/"
local tmp_data_path "./temp/`dvs'/en/"

local allfiles : dir "`ori_data_path'" files "*.dta"
foreach file in `allfiles' {
  use "`ori_data_path'`file'", clear
  saveold "`tmp_data_path'`file'", replace
}
