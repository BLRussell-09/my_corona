import requests
import sys

class State:

  def __init__(self, state_arr):
    self.active = state_arr['active']
    self.cases = state_arr['cases']
    self.deaths = state_arr['deaths']
    self.state = state_arr['state']
    self.todayCases = state_arr['todayCases']
    self.todayDeaths = state_arr['todayDeaths']

class JHU_County:
  def __init__(self, county):
    self.country = county['country']
    self.province = county['province']
    self.city = county['city']
    self.updatedAt = county['updatedAt']
    self.confirmed = county['stats']['confirmed']
    self.deaths = county['stats']['deaths']
    self.recovered = county['stats']['recovered']


def get_all_state_data(name):
  r = requests.get('https://corona.lmao.ninja/states') # Returns an array of Corona data by state
  res = r.json()
  data = next((elem for elem in res if elem['state'] == name), None)

  state_data = State(data)

  return state_data

def get_county_data(state):
  r = requests.get('https://corona.lmao.ninja/jhucsse')
  res = r.json()
  county_arr = []

  for county in res:
    if county['province'] == state:
      county_data = JHU_County(county)
      county_arr.append(county_data)

  return county_arr

def print_report(state):
  state_data = get_all_state_data(state)
  county_data = get_county_data(state)

  print(f'{state}:')
  print(f'Total cases: {state_data.cases}')
  print('---------------------------------')
  for county in county_data:
    print(f'{county.city}: {county.confirmed} confirmed cases')

# get_all_state_data(sys.argv[1])
# get_county_data(sys.argv[1])
print_report("sys.argv[1]")