from ...models.ticket import Ticket


def get_important_information(ticket: Ticket):
    print ('this is very important -> '+ str(ticket.price) + ' €')
    print ('Show concert name -> '+ ticket.show)
