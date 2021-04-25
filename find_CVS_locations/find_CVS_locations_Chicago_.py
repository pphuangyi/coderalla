#! /usr/bin/env python

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
from pathlib import Path

###### User info here

# GPS location
my_loc = (41.840573846853516, -87.63928590242628)

# rough distances per GPS coord near this location
miles_per_lat = 69.1
miles_per_lon = 52.93

# path to chrome driver (or other browser driver)
# for Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
# for others: https://selenium-python.readthedocs.io/installation.html
chromedriver_path = Path('C:/Users/pipih/Documents/Drives')
print(chromedriver_path.exists())

# path to write list of found appointments to
output_path = './output_Chicago'

###### Use Selenium to scrape CVS info timed loop
while True:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f'\nChecking for appointments at {current_time}')

    # Get current appointment availability
    url = 'https://www.cvs.com/immunizations/covid-19-vaccine?icid=cvs-home-hero1-link2-coronavirus-vaccine'
    timestamp_xpath = '//*[@id="vaccineinfo-NY"]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[5]/div/p[1]'
    ny_data_xpath = '//*[@id="vaccineinfo-NY"]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody'

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--log-level=3')

    driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver_path)
    driver.get(url)
    driver.find_element_by_link_text('New York').click()

    # timestamp
    timestamp = driver.find_element_by_xpath(timestamp_xpath).text
    timestamp = timestamp.split('.')[0]
    print(f"\n{timestamp}")

    # data
    data = driver.find_element_by_xpath(ny_data_xpath).text
    driver.quit()
    cvs_locs = [line.split(', NY ') for line in data.split('\n')]

    # get open locations with GPS coords
    locations = []
    for loc in cvs_locs:
        name = loc[0]
        available_appointments = loc[1] == 'Available'
        if not available_appointments:
            continue
        
        if name in towns:
            county = towns[name][1]
            gps = towns[name][5]
            locations.append([name + ', NY', county, gps])
        elif name in villages:
            county = villages[name][1]
            gps = villages[name][5]
            locations.append([name + ', NY', county, gps])
        elif name in places:
            county = places[name][1]
            gps = places[name][5]
            locations.append([name + ', NY', county, gps])
        else:
            locations.append([name + ', NY', '', ''])

    print(f'Found {len(locations)} CVS locations with appointments available:')
    for l in locations:
        print(f'\t{l[0]}')

    local_count = 0
    for i, loc in enumerate(locations):
        #compute estimated distance from GPS coords
        if loc[1] == 'Nassau' or loc[1] == 'Suffolk':
            loc_coord = loc[2].split(',')
            loc_lat = float(loc_coord[0])
            loc_lon = float(loc_coord[1])
            dist_lat = (loc_lat - my_lat) * miles_per_lat
            dist_lon = (loc_lon - my_lon) * miles_per_lon
            dist = (dist_lat * dist_lat + dist_lon * dist_lon) ** (1/2)
            # replace gps entry with estimated distance
            locations[i][2] = str(round(dist,1))
            local_count += 1
        else:
            # remove for non-local places
            locations[i][2] = ''

    print(f'{local_count} within Nassau and Suffolk counties:')

    local = [loc for loc in locations if loc[2]]
    if local:
        timestamp = timestamp[13:].replace(':',' ').split(' ')
        outfilename = 'appointments_found_' + '_'.join(timestamp) + '.txt'
        with open(os.path.join(output_path, outfilename), 'w') as outfile:
            local.sort(key = lambda loc:float(loc[2]))
            for loc in local:
                print(f'\t{loc[0]}\t{loc[2]} miles')
                outfile.write(f'\t{loc[0]}\t{loc[2]} miles\n')
    
    # check every 15 minutes (CVS official info refreshes at this rate)
    print('\nChecking again in 15 minutes...')
    time.sleep(900)