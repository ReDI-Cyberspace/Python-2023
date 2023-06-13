from folder.subfolder.functions import get_important_information as info_ticket
# from models.ticket import Ticket # as ticket


madonna_ticket  = Ticket(34, 'madonna ticket')

madonna_ticket_noname  = Ticket(34)


info_ticket(madonna_ticket)

info_ticket(madonna_ticket_noname)