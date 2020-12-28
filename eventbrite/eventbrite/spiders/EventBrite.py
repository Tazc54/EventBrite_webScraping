import scrapy
from ..items import EventbriteItem


class EventbriteSpider(scrapy.Spider):
    name = 'EventBrite'
    start_urls = ['https://www.eventbrite.com/d/united-states/business--events/?page=1']
    page_number = 0

    def start_requests(self):
        for page in range(1, 10):
            if self.page_number < 10:
                self.page_number += 1
                yield scrapy.Request(url=f'https://www.eventbrite.com/d/united-states/all-events/?page={page}',
                                     callback=self.parse_urls)

    def parse_urls(self, response):
        events_urls = response.css('.eds-event-card-content--fixed .eds-event-card-content__primary-content '
                                   '.eds-event-card-content__action-link').css('::attr(href)').getall()
        for events in events_urls:
            yield scrapy.Request(events, callback=self.parse)

    def parse(self, response, **kwargs):
        self.logger.warning('Parse function called on %s', response.url)
        items = EventbriteItem()
        items['event_name'] = response.css('.listing-hero-title').css('::text').get()
        items['event_start_date'] = response.css('.js-date-time-first-line').css('::text').get()
        items['event_start_time'] = response.css('.js-date-time-second-line ').css('::text').get()
        items['event_end_date'] = response.css('.js-date-time-first-line').css('::text').get()
        items['event_end_time'] = response.css('.js-date-time-second-line ').css('::text').get()
        even_location_list = response.css('.event-details__data:nth-child(4)').css('::text').getall()
        event_location_list = [item for item in even_location_list if '\n' not in item and '\t' not in item]
        items['event_location'] = event_location_list
        items['event_url'] = response.url
        event_organizer = response.css('.listing-organizer-name').css('::text').get()
        if event_organizer is not None:
            event_organizer = event_organizer.strip()
        items['event_organizer'] = event_organizer
        image_url = response.css('.listing-hero.listing-hero--bkg picture').css('::attr(content)').get()
        if image_url is not None:
            items['image_urls'] = [image_url]
        yield items

