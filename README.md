This repository contents IMI metering fraud project.


Testing area: Northern, area 3
# cleansing data process
At first we observed that the size of Excel file is too large (~around 9 GB, ~70m rows), so we separated into 75 small files using program CSV splitter.

## in 1_1 Retrieve kWhr data and metering fraud data.pynb
We started looking through each file, there is 'Note_read' column which content indicator of normal, abnormal meter.
Examples are '0000' for normal, '0600' for malfunction meter, '1100' for fraud metering, '7700' for empty house,
and '8800' for false alarm.
Consequently, we extract interest 'Note_read' in difference json file which are, normal (temp_dict_normal_detect.json), fraud (temp_dict_fraud_detect.json), empty house (temp_dict_empty_house_detect.json), false alarm (temp_dict_false_alarm_detect.json).
It take about 30 minutes to develop each json file.


after cleansing process, we found that number of fraud metering is 243 data, empty house is 3,896,732 data, 6,146,278 data,

## data visualization for cleansing data
in 1_2 show maps.pynb

# feature extraction

number of zero crossing of normalize standard deviation over 6 months






<div style="width:830px; background-color:white; height:120px; overflow:auto;">
  <img src="Images/map (1).png" width="600" height="600">
</div>
<span style="color:blue">Blue:  year *2016* </span>

<span style="color:red">Red: year *2017* </span>

<span style="color:orange">Orange: year *2018* </span>

<span style="color:green">Green: year *2019* </span>





Phase 1:
 * N3


Contributions:
  * cleansing measurement data from UCUE as seen in dict_measurement_N3.json




Group members:

<div style="width:830px; background-color:white; height:120px; overflow:auto;">
  <div style="width: 2000px; height: 90px;">
    <img src="member/1.png" width="200" height="200">
    <img src="member/2.png" width="200" height="200">
    <img src="member/3.png" width="200" height="200">
    <img src="member/4.png" width="200" height="200">
    <img src="member/5.png" width="200" height="200">
    <img src="member/6.png" width="200" height="200">
    <img src="member/7.png" width="200" height="200">
    <img src="member/8.png" width="200" height="200">
    <img src="member/9.png" width="200" height="200">
    <img src="member/10.png" width="200" height="200">
    <img src="member/11.png" width="200" height="200">
  </div>
</div>
