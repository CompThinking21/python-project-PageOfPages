from radar import RadarClient
import requests
from time import sleep


# initialize client with your project's secret key
SECRET_KEY = "prj_live_sk_9e32c80a5ead6974670df24b831fd00ca48c183e"
PUB_KEY = "prj_live_pk_b4cede5fbe2f41ae7d329ae59f9a155944fed53e"
radar = RadarClient(secret_key=SECRET_KEY, pub_key=PUB_KEY)


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


# **** Radar.io API **** #
'''
Query User for zipcode. 
    - Read out promt to user explaining what this program does and returning the 
      City and State of the zip code.
    - Return longitude/latitude 
'''
def user_location():
    print("\n\t\t\t   Neighborhood Search")
    print("- the best way to know what you should really expect from your Neighborhood. -\n")
    sleep(5)
    print("Moving somewhere new? Do you already live somewhere and don't fully get the")
    print("layout of where you live?\n")
    sleep(7)
    print("Or, are you curious about what it's like to live in other areas?\n")
    sleep(7)
    print("Neighborhood Search is here to answer these questions by giving you the ")
    print("relevent data YOU need.\n")
    sleep(5)
    print("We hope this can help to educate you, make you more aware, and to inform you!\n")
    sleep(5)


    confirmation = "no"
    while (confirmation.lower() == "no"):
        print("Input the Address you'd like to search: ")
        input_home_address = input().replace(" ", "+")

        site_address ='https://api.radar.io/v1/search/autocomplete?query={}&layers=fine'.format(input_home_address)
        data = {'Authorization': PUB_KEY}
        home_address = requests.get(site_address, headers=data)     #Address is a json array of addresses similiar to the address inpu by user. 
                                                                    #First result is one closests to the users IP address

        confirmation = " "
        while (confirmation.lower() != "no" and confirmation.lower() != "yes"):
            print("\nPlease Confirm (Yes/No) if this is your Address:  \n" + home_address.json()['addresses'][0]['formattedAddress'] + "\n\nConfirmation (yes/no): ")  
            confirmation = input()

        if (confirmation.lower() == "no"):
            print("\nTo return the address you are looking for, please be more specific. Make sure your")
            print("spelling is correct and include the State in which the address you are looking for is.\n")
            # print("and include the State in which the address you are looking for is.\n")
            sleep(5)

    
    lat = home_address.json()['addresses'][0]['latitude']
    lng = home_address.json()['addresses'][0]['longitude']
    
    return (lat,lng)


'''
Given long/latitude data (retrieved from user_location once user inputs a zip),
Return data based on Address
'''
class Data:

    coordinates = user_location()

    
    # Currently, in order to get transporatation and food near an address, I need to use Google Places API which costs money
    # '''
    # Local transportation
    # Radar.io API
    # '''
    # def transport():
    #     return 0
        
    # '''
    # Local food and grocerery shops
    # Radar.io API
    # '''
    # def food():
    #     return 0

    #---------------------General City Data----------------------#
    # **** Data USA API **** #
    '''
    City data on race/ethnicity
    '''
    def race_eth():
        return 0

    '''
    City data on health
    '''
    def health():
        return 0

    '''
    City data on jobs
    '''
    def jobs():
        return 0

    '''
    City data on comute time
    '''
    def comute_time():
        return 0

    '''
    City data on *** ect, anything else I might want to add here***
    '''
    def ect():
        return 0

    #----------Rent----------#

    '''
    City data on percentage of rent vs. owned 
    '''
    def rent_vs_owned():
        return 0

    '''
    City data on rent average cost
    '''
    def rent_cost():
        return 0

    #-------Economy----------#

    '''
    City data on wages 
    '''
    def wage():
        url = "http://api.datausa.io/api/?show=geo&sumlevel=state&required=avg_wage"

        json = requests.get(url).json()

        # data = [dict(zip(json["headers"], d)) for d in json["data"]]

    
    '''
    City data on income by location 
    '''
    def location_income():
        return 0

    '''
    City data on most common occumpations
    Return a list of top 15 ocupation by general category
    '''
    def occupations():
        return 0

    
    #--------------------------Costs------------------------------#
    # **** Grocerybear API **** #
    '''
    Regional data on average grocery costs
    '''
    def grocery_cost():
        return 0

    # **** HERE Fuel Prices API **** #
    '''
    Regional data on average gas costs
    '''
    def gas_costs():
        return 0
    

    '''
    Return apartment lsitings with beds, baths, location based on Zipcode with a 10 mile radius.

    Sort listings based on cheapest to most expensive. Give overview of more expensive listing - stating 
    something like "80 apartments in this area priced over $2,000 per month".
    '''
    def apartment_listings():
        return 0
    

'''
first call UserLocation to get user zip:
then create an object of that zip and retrive data
Formally read out a prompt for each data call such as 
for occupations say "The top ocuppations in your area are..."
'''
def main():
    print("\n----------------------------------------COMPLETE!-----------------------------------------")
    print("At this stage in the project, I have been able to use Radar API to confirm the address the")
    print("user puts in. I still have yet to retrieve data from other APIs. Below are API's I plan to  ")
    print("call for varied data describing the city of the user's inputted address:")
    print("\t- Data USA API for the following city statistics")
    print("\t\t- race/ethnicity")
    print("\t\t- health")
    print("\t\t- jobs")
    print("\t\t- comute timee")
    print("\t\t- rent vs owned")
    print("\t\t- rent_cost")
    print("\t\t- wage")
    print("\t\t- income")
    print("\t\t- occupation")
    print("\t- Grocerybear API for average Grocerry costs")
    print("\t- HERE Fuel Prices API for average Gas costs")


if __name__ == "__main__": 
    main()