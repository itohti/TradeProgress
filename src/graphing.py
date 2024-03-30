# This will be used for all graphing code.

# There will be daily, weekly, monthly, and yearly charts so organize the time data accordingly.


### BASE CODE it doesnt work as intended :P
import fetchData
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime
import pandas as pd
fig, ax = plt.subplots()
accounts = []
accounts = fetchData.main()
x = []
y = []
for i in accounts[0].historic_balance:
    x.append(i[0][:-6])
    y.append(i[1])
line_graph = ax.plot(x, y)[0]
ax.legend()
# This will update the data for any open positions.
def update_data(account):
    if (account.has_openPositions):
       fetchData.fetch_unrealized_pl(account)
       account.historic_balance.append((datetime.datetime.now().isoformat(), account.unrealized_pl + account.accountBalance))

def update(frame):
    update_data(accounts[0])
    for i in accounts[0].historic_balance:
        x.append(i[0][:-6])
        y.append(i[1])
    line_graph.set_xdata(x[:frame])
    line_graph.set_ydata(y[:frame])

    return line_graph

ani = FuncAnimation(fig=fig, func=update, frames=60)
plt.show()