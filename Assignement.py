class WebsiteHitCounter:
    def __init__(self):
        self.customer_visits = {}
        self.website_visit_count = {}

    def VisitWebsite(self, customerId, deviceId, websiteId):
        if customerId not in self.customer_visits:
            self.customer_visits[customerId] = {}
        if websiteId not in self.customer_visits[customerId]:
            self.customer_visits[customerId][websiteId] = set()

     
        if deviceId not in self.customer_visits[customerId][websiteId]:
            self.customer_visits[customerId][websiteId].add(deviceId)
            if websiteId not in self.website_visit_count:
                self.website_visit_count[websiteId] = 0
            self.website_visit_count[websiteId] += 1

    def GetWebsiteVisitCountForCustomer(self, customerId, websiteId):
        if customerId in self.customer_visits and websiteId in self.customer_visits[customerId]:
            return len(self.customer_visits[customerId][websiteId])
        return 0

    def GetOverallWebsiteHitCount(self, websiteId):
        if websiteId in self.website_visit_count:
            return self.website_visit_count[websiteId]
        return 0


def main():
    counter = WebsiteHitCounter()

    counter.VisitWebsite("cust1", "dev1", "site1")
    counter.VisitWebsite("cust1", "dev2", "site1")
    counter.VisitWebsite("cust1", "dev1", "site1")
    counter.VisitWebsite("cust2", "dev3", "site1")
    counter.VisitWebsite("cust2", "dev3", "site2")

    print(counter.GetWebsiteVisitCountForCustomer("cust1", "site1"))  
    print(counter.GetWebsiteVisitCountForCustomer("cust2", "site1"))  
    print(counter.GetWebsiteVisitCountForCustomer("cust2", "site2"))  

    print(counter.GetOverallWebsiteHitCount("site1"))  
    print(counter.GetOverallWebsiteHitCount("site2"))  

if __name__ == "__main__":
    main()
