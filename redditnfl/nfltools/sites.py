import pytz
"""
Time zone and yr.no location code for all stadiums used by the NFL
"""

EST = pytz.timezone('US/Eastern')
CST = pytz.timezone('US/Central')
PST = pytz.timezone('US/Pacific')
MST_NODST = pytz.timezone('US/Arizona') # No DST
MST = pytz.timezone('America/Denver')
GMT = pytz.timezone('Europe/London')

sites = {
        'Gillette Stadium': [EST, 'United_States/Massachusetts/Foxborough', ['NE'], (42.090944,-71.264344)],
        'Georgia Dome': [EST, 'United_States/Georgia/Atlanta', []],
        'Mercedes-Benz Stadium': [EST, 'United_States/Georgia/Atlanta', ['ATL'], (33.755,-84.401)],
        'AT&T Stadium': [CST, 'United_States/Texas/Arlington', ['DAL'], (32.747778,-97.092778)],
        'Arrowhead Stadium': [CST, 'United_States/Missouri/Kansas_City', ['KC'], (39.048889,-94.483889)],
        'Lambeau Field': [CST, 'United_States/Wisconsin/Green_Bay', ['GB'], (44.501389,-88.062222)],
        'NRG Stadium': [CST, 'United_States/Texas/Houston', ['HOU'], (29.684722,-95.410833)],
        'CenturyLink Field': [PST, 'United_States/Washington/Seattle', ['SEA'], (47.5952,-122.3316)],
        'New Era Field': [EST, 'United_States/New_York/Orchard_Park~5129951', ['BUF'], (42.774,-78.787)],
        'Nissan Stadium': [CST, 'United_States/Tennessee/Nashville', ['TEN'], (36.166389,-86.771389)],
        'Lincoln Financial Field': [EST, 'United_States/Pennsylvania/Philadelphia', ['PHI'], (39.900833,-75.1675)],
        'Hard Rock Stadium': [EST, 'United_States/Florida/Miami_Gardens', ['MIA'], (25.958056,-80.238889)],
        'EverBank Field': [EST, 'United_States/Florida/Jacksonville', []],
        'TIAA Bank Field': [EST, 'United_States/Florida/Jacksonville', ['JAX'], (30.323889,-81.6375)],
        'Lucas Oil Stadium': [EST, 'United_States/Indiana/Indianapolis', ['IND'], (39.760056,-86.163806)],
        'Bank of America Stadium': [EST, 'United_States/North_Carolina/Charlotte', ['CAR'], (35.225833,-80.852778)],
        'FirstEnergy Stadium': [EST, 'United_States/Ohio/Cleveland', ['CLE'], (41.506111,-81.699444)],
        'Ford Field': [EST, 'United_States/Michigan/Detroit', ['DET'], (42.34,-83.045556)],
        'Levi\'s Stadium': [PST, 'United_States/California/Santa_Clara', []],
        u'Levi\'s® Stadium': [PST, 'United_States/California/Santa_Clara', ['SF'], (37.403,-121.97)],
        'Raymond James Stadium': [EST, 'United_States/Florida/Tampa', ['TB'], (27.975833,-82.503333)],
        'Los Angeles Memorial Coliseum': [PST, 'United_States/California/Los_Angeles', ['LA'], (34.014167,-118.287778)],
        'MetLife Stadium': [EST, 'United_States/New_Jersey/East_Rutherford', ['NYG', 'NYJ'], (40.813528,-74.074361)],
        'Soldier Field': [CST, 'United_States/Illinois/Chicago', ['CHI'], (41.8623,-87.6167)],
        'M&T Bank Stadium': [EST, 'United_States/Maryland/Baltimore', ['BAL'], (39.278056,-76.622778)],
        'Paul Brown Stadium': [EST, 'United_States/Ohio/Cincinnati', ['CIN'], (39.095,-84.516)],
        'U.S. Bank Stadium': [CST, 'United_States/Minnesota/Minneapolis', ['MIN'], (44.974,-93.258)],
        'University of Phoenix Stadium': [MST_NODST, 'United_States/Arizona/Glendale', []],
        'State Farm Stadium': [MST_NODST, 'United_States/Arizona/Glendale', ['ARI'], (33.5275,-112.2625)],
        'Qualcomm Stadium': [PST, 'United_States/California/San_Diego', []],
        'StubHub Center': [PST, 'United_States/California/Carson', []],
        'Dignity Health Sports Park': [PST, 'United_States/California/Carson', ['LAC'], (33.864,-118.261)],
        'ROKiT Field at StubHub Center': [PST, 'United_States/California/Carson', []],
        'Sports Authority Field at Mile High': [MST, 'United_States/Colorado/Denver', []],
        'Broncos Stadium at Mile High': [MST, 'United_States/Colorado/Denver', ['DEN'], (39.743889,-105.02)],
        'FedExField': [EST, 'United_States/Maryland/Landover', ['WAS'], (38.907778,-76.864444)],
        'Oakland Coliseum': [PST, 'United_States/California/Oakland', ['OAK'], (37.751667,-122.200556)],
        'Oakland-Alameda County Coliseum': [PST, 'United_States/California/Oakland', ['OAK'], (37.751667,-122.200556)],
        'Mercedes-Benz Superdome': [CST, 'United_States/Louisiana/New_Orleans', ['NO'], (29.950833,-90.081111)],
        'Heinz Field': [EST, 'United_States/Pennsylvania/Pittsburgh', ['PIT'], (40.446667,-80.015833)],

        'Estadio Azteca': [pytz.timezone('America/Mexico_City'), 'Mexico/Distrito_Federal/Mexico_City', []],
        'Estadio Azteca (Mexico City)': [pytz.timezone('America/Mexico_City'), 'Mexico/Distrito_Federal/Mexico_City', []],
        'Wembley Stadium': [GMT, 'United_kingdom/England/London', []],
        'Twickenham Stadium': [GMT, 'United_kingdom/England/London', []],
        'Tom Benson Hall of Fame Stadium': [EST, 'United_States/Ohio/Canton', []],
        'Camping World Stadium': [EST, 'United_States/Florida/Orlando', []],
        }


def by_name(lookup_name):
    for name, data in sites.items():
        if name == lookup_name:
            return (name, data)


def by_team(lookup_team):
    if 'abbr' in lookup_team:
        lookup_team = lookup_team['abbr']
    for name, data in sites.items():
        if lookup_team in data[2]:
            return (name, data)


def main():
    import sys
    from pprint import pprint
    if sys.argv[1] == 'team':
        for team in sys.argv[2:]:
            print(team)
            pprint(by_team(team))
    elif sys.argv[1] == 'name':
        for name in sys.argv[2:]:
            print(name)
            pprint(by_name(name))
    else:
        print("Unknown: %r" % sys.argv)


if __name__ == "__main__":
    main()
