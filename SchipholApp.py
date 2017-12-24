
import requests
import sys
import wx

# make sure you got pyopenssl, ndg-httpsclient and pyasn1 installed

class ExampleFrame(wx.Frame):
    def __init__(self, parent):

        wx.Frame.__init__(self, parent)

        self.panel = wx.Panel(self)
        fontbold = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD)

        self.lbl_date = wx.StaticText(self.panel, label="Date [yyyy-mm-dd]:")
        self.input_date = wx.TextCtrl(self.panel, size=(140, -1))

        self.lbl_flight = wx.StaticText(self.panel, label="Flight [i.e KL4302]:")
        self.input_flight = wx.TextCtrl(self.panel, size=(140, -1))

        self.button = wx.Button(self.panel, label="Retrieve data")

        # Generic info

        self.lbl_result_flight = wx.StaticText(self.panel, label="Flight:")
        self.result_flight = wx.StaticText(self.panel, label="")
        self.result_flight.SetForegroundColour(wx.RED)

        self.lbl_airline = wx.StaticText(self.panel, label="Airline:")
        self.airline = wx.StaticText(self.panel, label="")
        self.airline.SetForegroundColour(wx.RED)

        self.lbl_direction = wx.StaticText(self.panel, label="Arrival or Departure?:")
        self.direction = wx.StaticText(self.panel, label="")
        self.direction.SetForegroundColour(wx.RED)

        self.lbl_route = wx.StaticText(self.panel, label="Route / Destinations:")
        self.route = wx.StaticText(self.panel, label="")
        self.route.SetForegroundColour(wx.RED)

        self.lbl_type = wx.StaticText(self.panel, label="Aircraft Type:")
        self.type = wx.StaticText(self.panel, label="")
        self.type.SetForegroundColour(wx.RED)

        self.lbl_status = wx.StaticText(self.panel, label="Status:")
        self.status = wx.StaticText(self.panel, label="")
        self.status.SetForegroundColour(wx.RED)

        # Arrival details

        self.lbl_arrival = wx.StaticText(self.panel, label="Arrival Details")
        self.lbl_arrival.SetFont(fontbold)

        self.lbl_estimated_landing_time = wx.StaticText(self.panel, label="Estimated landing time:")
        self.estimated_landing_time = wx.StaticText(self.panel, label="")
        self.estimated_landing_time.SetForegroundColour(wx.RED)

        self.lbl_actual_landing_time = wx.StaticText(self.panel, label="Actual landing time:")
        self.actual_landing_time = wx.StaticText(self.panel, label="")
        self.actual_landing_time.SetForegroundColour(wx.RED)

        self.lbl_arrival_terminal = wx.StaticText(self.panel, label="Terminal:")
        self.arrival_terminal = wx.StaticText(self.panel, label="")
        self.arrival_terminal.SetForegroundColour(wx.RED)

        self.lbl_arrival_gate = wx.StaticText(self.panel, label="Gate:")
        self.arrival_gate = wx.StaticText(self.panel, label="")
        self.arrival_gate.SetForegroundColour(wx.RED)

        self.lbl_expected_belt = wx.StaticText(self.panel, label="Expected time on belt:")
        self.expected_belt = wx.StaticText(self.panel, label="")
        self.expected_belt.SetForegroundColour(wx.RED)

        self.lbl_belt = wx.StaticText(self.panel, label="Baggage belt:")
        self.belt = wx.StaticText(self.panel, label="")
        self.belt.SetForegroundColour(wx.RED)

        # Departure details

        self.lbl_departure = wx.StaticText(self.panel, label="Departure Details")
        self.lbl_departure.SetFont(fontbold)

        self.lbl_scheduled_time = wx.StaticText(self.panel, label="Scheduled departure time:")
        self.scheduled_time = wx.StaticText(self.panel, label="")
        self.scheduled_time.SetForegroundColour(wx.RED)

        self.lbl_actual_departure_time = wx.StaticText(self.panel, label="Actual departure time:")
        self.actual_departure_time = wx.StaticText(self.panel, label="")
        self.actual_departure_time.SetForegroundColour(wx.RED)

        self.lbl_departure_terminal = wx.StaticText(self.panel, label="Terminal:")
        self.departure_terminal = wx.StaticText(self.panel, label="")
        self.departure_terminal.SetForegroundColour(wx.RED)

        self.lbl_departure_gate = wx.StaticText(self.panel, label="Gate:")
        self.departure_gate = wx.StaticText(self.panel, label="")
        self.departure_gate.SetForegroundColour(wx.RED)

        self.lbl_gate_open = wx.StaticText(self.panel, label="Expected time gate open:")
        self.gate_open = wx.StaticText(self.panel, label="")
        self.gate_open.SetForegroundColour(wx.RED)

        self.lbl_gate_closed = wx.StaticText(self.panel, label="Expected time gate closing:")
        self.gate_closed = wx.StaticText(self.panel, label="")
        self.gate_closed.SetForegroundColour(wx.RED)

        # Set sizer for the frame, so we can change frame size to match widgets

        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)

        # Set sizer for the panel content

        self.sizer = wx.GridBagSizer(10, 5)

        self.sizer.Add(self.lbl_date, (1, 0))
        self.sizer.Add(self.input_date, (1, 1))

        self.sizer.Add(self.lbl_flight, (2, 0))
        self.sizer.Add(self.input_flight, (2, 1))

        self.sizer.Add(self.button, (4, 0), (1, 2), flag=wx.EXPAND)

        self.sizer.Add(self.lbl_result_flight, (6, 0))
        self.sizer.Add(self.result_flight, (6, 1))

        self.sizer.Add(self.lbl_airline, (7, 0))
        self.sizer.Add(self.airline, (7, 1))

        self.sizer.Add(self.lbl_direction, (8, 0))
        self.sizer.Add(self.direction, (8, 1))

        self.sizer.Add(self.lbl_route, (9, 0))
        self.sizer.Add(self.route, (9, 1))

        self.sizer.Add(self.lbl_type, (10, 0))
        self.sizer.Add(self.type, (10, 1))

        self.sizer.Add(self.lbl_status, (11, 0))
        self.sizer.Add(self.status, (11, 1))

        # Arrival details

        self.sizer.Add(self.lbl_arrival, (13, 0))

        self.sizer.Add(self.lbl_estimated_landing_time, (15, 0))
        self.sizer.Add(self.estimated_landing_time, (15, 1))

        self.sizer.Add(self.lbl_actual_landing_time, (16, 0))
        self.sizer.Add(self.actual_landing_time, (16, 1))

        self.sizer.Add(self.lbl_arrival_terminal, (17, 0))
        self.sizer.Add(self.arrival_terminal, (17, 1))

        self.sizer.Add(self.lbl_arrival_gate, (18, 0))
        self.sizer.Add(self.arrival_gate, (18, 1))

        self.sizer.Add(self.lbl_expected_belt, (19, 0))
        self.sizer.Add(self.expected_belt, (19, 1))

        self.sizer.Add(self.lbl_belt, (20, 0))
        self.sizer.Add(self.belt, (20, 1))

        # Departure details

        self.sizer.Add(self.lbl_departure, (13, 6))

        self.sizer.Add(self.lbl_scheduled_time, (15, 6))
        self.sizer.Add(self.scheduled_time, (15, 7))

        self.sizer.Add(self.lbl_actual_departure_time, (16, 6))
        self.sizer.Add(self.actual_departure_time, (16, 7))

        self.sizer.Add(self.lbl_departure_terminal, (17, 6))
        self.sizer.Add(self.departure_terminal, (17, 7))

        self.sizer.Add(self.lbl_departure_gate, (18, 6))
        self.sizer.Add(self.departure_gate, (18, 7))

        self.sizer.Add(self.lbl_gate_open, (19, 6))
        self.sizer.Add(self.gate_open, (19, 7))

        self.sizer.Add(self.lbl_gate_closed, (20, 6))
        self.sizer.Add(self.gate_closed, (20, 7))

        # Set simple sizer for a nice border

        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)

        # Use the sizers

        self.panel.SetSizerAndFit(self.border)
        self.SetSizerAndFit(self.windowSizer)

        # Set event handlers

        self.button.Bind(wx.EVT_BUTTON, self.on_button)

    def on_button(self, e):

        # Get date and fligth number

        self.datenext = self.input_date.GetValue()
        self.flightnext = self.input_flight.GetValue()

        # Insert API id & API key

        self.api_id = ""
        self.api_key = ""

        url = "https://api.schiphol.nl/public-flights/flights"
        querystring = {"app_id": "%s" % self.api_id, "app_key": "%s" % self.api_key,
                       "scheduledate": "%s" % self.datenext, "flightname": "%s" % self.flightnext}
        headers = {
            'resourceversion': "v3"
        }

        # Get data

        try:
            response = requests.request("GET", url, headers=headers, params=querystring)

        except requests.exceptions.ConnectionError as error:
            print(error)
            sys.exit()

        if response.status_code == 200:
            flightList = response.json()

            self.result_flight.SetLabel(flightList["flights"][0]["flightName"])
            self.airline.SetLabel(flightList["flights"][0]["prefixICAO"])

            self.direction.SetLabel("Arrival") if flightList["flights"][0]["flightDirection"] == "A" else self.direction.SetLabel("Departure")

            if len(flightList["flights"][0]["route"]["destinations"]) == 1:
                self.route.SetLabel(flightList["flights"][0]["route"]["destinations"][0])

            elif len(flightList["flights"][0]["route"]["destinations"]) == 2:
                self.route.SetLabel(
                    str(flightList["flights"][0]["route"]["destinations"][0]) + " " + str(
                        flightList["flights"][0]["route"]["destinations"][1]))

            elif len(flightList["flights"][0]["route"]["destinations"]) == 3:
                self.route.SetLabel(
                    str(flightList["flights"][0]["route"]["destinations"][0]) + " " + str(
                    flightList["flights"][0]["route"]["destinations"][1]) + " " + str(
                    flightList["flights"][0]["route"]["destinations"][2]))

            else:
                self.route.SetLabel("Too many destinations")

            self.type.SetLabel(flightList["flights"][0]["aircraftType"]["iatamain"])

            # Set public states

            if len(flightList["flights"][0]["publicFlightState"]["flightStates"]) == 1:
                self.status.SetLabel(flightList["flights"][0]["publicFlightState"]["flightStates"][0])

            elif len(flightList["flights"][0]["publicFlightState"]["flightStates"]) == 2:
                self.status.SetLabel(
                    str(flightList["flights"][0]["publicFlightState"]["flightStates"][0]) + " " + str(
                        flightList["flights"][0]["publicFlightState"]["flightStates"][1]))

            elif len(flightList["flights"][0]["publicFlightState"]["flightStates"]) == 3:
                self.status.SetLabel(
                    str(flightList["flights"][0]["publicFlightState"]["flightStates"][0]) + " " + str(
                        flightList["flights"][0]["publicFlightState"]["flightStates"][1]) + " " + str(
                        flightList["flights"][0]["publicFlightState"]["flightStates"][2]))

            elif len(flightList["flights"][0]["publicFlightState"]["flightStates"]) == 4:
                self.status.SetLabel(
                    str(flightList["flights"][0]["publicFlightState"]["flightStates"][0]) + " " + str(
                        flightList["flights"][0]["publicFlightState"]["flightStates"][1]) + " " + str(
                        flightList["flights"][0]["publicFlightState"]["flightStates"][2]) + " " + str(
                        flightList["flights"][0]["publicFlightState"]["flightStates"][3]))

            else:
                self.status.SetLabel("Too many statuses")

            # Apply arrival data

            if flightList["flights"][0]["flightDirection"] == "A":

                self.estimated_landing_time.SetLabel(flightList["flights"][0]["estimatedLandingTime"])

                self.actual_landing_time.SetLabel(flightList["flights"][0]["actualLandingTime"])

                try:
                    self.arrival_terminal.SetLabel(str(flightList["flights"][0]["terminal"]))
                except:
                    self.arrival_terminal.SetLabel("Not yet known")

                try:
                    self.arrival_gate.SetLabel(flightList["flights"][0]["gate"])
                except:
                    self.arrival_gate.SetLabel("Not yet known")

                try:
                    self.expected_belt.SetLabel(str(flightList["flights"][0]["expectedTimeOnBelt"]))
                except:
                    self.expected_belt.SetLabel("Not yet known")

                try:
                    self.belt.SetLabel(flightList["flights"][0]["baggageClaim"]["belts"][0])
                except:
                    self.belt.SetLabel("Not yet known")

                self.scheduled_time.SetLabel("")
                self.actual_departure_time.SetLabel("")
                self.departure_terminal.SetLabel("")
                self.departure_gate.SetLabel("")
                self.gate_open.SetLabel("")
                self.gate_closed.SetLabel("")

            else:

                # Apply departure data

                self.scheduled_time.SetLabel(flightList["flights"][0]["scheduleTime"])

                try:
                    self.actual_departure_time.SetLabel(flightList["flights"][0]["actualOffBlockTime"])
                except:
                    self.actual_departure_time.SetLabel("Not yet known")

                try:
                    self.departure_terminal.SetLabel(str(flightList["flights"][0]["terminal"]))
                except:
                    self.departure_terminal.SetLabel("Not yet known")

                try:
                    self.departure_gate.SetLabel(flightList["flights"][0]["gate"])
                except:
                    self.departure_gate.SetLabel("Not yet known")

                try:
                    self.gate_open.SetLabel(str(flightList["flights"][0]["expectedTimeGateOpen"]))
                except:
                    self.gate_open.SetLabel("Not yet known")

                try:
                    self.gate_closed.SetLabel(str(flightList["flights"][0]["expectedTimeGateClosing"]))
                except:
                    self.gate_closed.SetLabel("Not yet known")

                self.estimated_landing_time.SetLabel("")
                self.actual_landing_time.SetLabel("")
                self.arrival_terminal.SetLabel("")
                self.arrival_gate.SetLabel("")
                self.expected_belt.SetLabel("")
                self.belt.SetLabel("")

        else:

            self.result_flight.SetLabel("This flight does not exist, please try again")

            self.airline.SetLabel("")
            self.direction.SetLabel("")
            self.route.SetLabel("")
            self.type.SetLabel("")
            self.status.SetLabel("")

            self.scheduled_time.SetLabel("")
            self.actual_departure_time.SetLabel("")
            self.departure_terminal.SetLabel("")
            self.departure_gate.SetLabel("")
            self.gate_open.SetLabel("")
            self.gate_closed.SetLabel("")

            self.estimated_landing_time.SetLabel("")
            self.actual_landing_time.SetLabel("")
            self.arrival_terminal.SetLabel("")
            self.arrival_gate.SetLabel("")
            self.expected_belt.SetLabel("")
            self.belt.SetLabel("")

app = wx.App(False)
frame = ExampleFrame(None)
frame.SetSize(0,0,1000,700)
frame.Center()
frame.Show()
app.MainLoop()