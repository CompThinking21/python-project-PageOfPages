'''given a zipcode, this program returns contextual data on the area such as:
    - local transportation
    - local food and grocerery shops
    - General City data on race/ethnicity, health, jobs, comute time, etc
    - General City data on renting
    - General City data on economy
        - Specific example of grocery and gas costs
    - Up to date apartment listings from cheapest to most expensive (with a cut off 
      at more expensive apartments. Will just give overview of those - stating "80 
      apartments in this area priced over $2,000 per month"
'''


'''
Query User for zipcode. 
Using Radar.io Geocoding API
    - Read out promt to user explaining what this program does and returning the 
      City and State of the zip code.
    - Return longitude/latitude 
'''
def user_location:


'''
Given long/latitude data (retrieved from user_location once user inputs a zip),
Return data based on Zip
'''
Class Zip_Data:

    '''
    Local transportation
    Radar.io API
    '''
    def transport:


    '''
    Local food and grocerery shops
    Radar.io API
    '''
    def food:

    #---------------------General City Data----------------------#
    # Get city data using Data USA API
    '''
    City data on race/ethnicity
    '''
    def race_eth:

    '''
    City data on health
    '''
    def health:

    '''
    City data on jobs
    '''
    def jobs:

    '''
    City data on comute time
    '''
    def comute_time:

    '''
    City data on *** ect, anything else I might want to add here***
    '''
    def ect:

    #----------Rent----------#

    '''
    City data on percentage of rent vs. owned 
    '''
    def rent_vs_owned:

    '''
    City data on rent average cost
    '''
    def rent_cost:

    #-------Economy----------#

    '''
    City data on wages 
    '''
    def wage:

    '''
    City data on income by location 
    '''
    def location_income:

    '''
    City data on most common occumpations
    Return a list of top 15 ocupation by general category
    '''
    def occupations:

    '''
    Regional data on average grocery costs
    '''
    def grocery_cost:

    '''
    Regional data on average gas costs
    '''
    def gas_costs:
    
    #------------------------------------------------------------#

    '''
    Return apartment lsitings with beds, baths, location based on Zipcode with a 10 mile radius.

    Sort listings based on cheapest to most expensive. Give overview of more expensive listing - stating 
    something like "80 apartments in this area priced over $2,000 per month".
    '''
    def apartment_listings:
    

'''
first call UserLocation to get user zip:
then create an object of that zip and retrive data
Formally read out a prompt for each data call such as 
for occupations say "The top ocuppations in your area are..."
'''
def main: