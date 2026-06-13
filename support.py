import matplotlib as plt
from matplotlib import pyplot
plt.use('Agg')
import io
import base64
def plot_2html(df_html,user_symbol,qtype):
    """type is 'stock' or 'economic'. """
    fig, ax = plt.pyplot.subplots()
    if qtype == 'stock':
        ax.plot(df_html['Close'], label=user_symbol, color='red')
    else:
        ax.plot(df_html, label=user_symbol, color='red')
    ax.legend()
    ax.grid(True)
    ax.set_title(f"{user_symbol} Stock Price")
    fig.autofmt_xdate()


    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    plt.pyplot.close(fig)

    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    return img_base64

country_dict = {
    "World": "WLD","Aruba": "ABW", "Afghanistan": "AFG", "Angola": "AGO", "Albania": "ALB", "Andorra": "AND",
    "United Arab Emirates": "ARE", "Argentina": "ARG", "Armenia": "ARM", "Antigua and Barbuda": "ATG",
    "Australia": "AUS", "Austria": "AUT", "Azerbaijan": "AZE", "Burundi": "BDI", "Belgium": "BEL",
    "Benin": "BEN", "Burkina Faso": "BFA", "Bangladesh": "BGD", "Bulgaria": "BGR", "Bahrain": "BHR",
    "Bahamas, The": "BHS", "Bosnia and Herzegovina": "BIH", "Belarus": "BLR", "Belize": "BLZ",
    "Bermuda": "BMU", "Bolivia": "BOL", "Brazil": "BRA", "Barbados": "BRB", "Brunei Darussalam": "BRN",
    "Bhutan": "BTN", "Botswana": "BWA", "Central African Republic": "CAF", "Canada": "CAN",
    "Switzerland": "CHE", "Chile": "CHL", "China": "CHN", "Cote d'Ivoire": "CIV", "Cameroon": "CMR",
    "Congo, Dem. Rep.": "COD", "Congo, Rep.": "COG", "Colombia": "COL", "Comoros": "COM",
    "Cape Verde": "CPV", "Costa Rica": "CRI", "Cuba": "CUB", "Curacao": "CUW", "Cyprus": "CYP",
    "Czech Republic": "CZE", "Germany": "DEU", "Djibouti": "DJI", "Dominica": "DMA", "Denmark": "DNK",
    "Dominican Republic": "DOM", "Algeria": "DZA", "Ecuador": "ECU", "Egypt, Arab Rep.": "EGY",
    "Eritrea": "ERI", "Spain": "ESP", "Estonia": "EST", "Ethiopia": "ETH", "Finland": "FIN",
    "Fiji": "FJI", "France": "FRA", "Micronesia, Fed. Sts.": "FSM", "Gabon": "GAB", "United Kingdom": "GBR",
    "Georgia": "GEO", "Ghana": "GHA", "Guinea": "GIN", "Gambia, The": "GMB", "Guinea-Bissau": "GNB",
    "Equatorial Guinea": "GNQ", "Greece": "GRC", "Grenada": "GRD", "Greenland": "GRL", "Guatemala": "GTM",
    "Guyana": "GUY", "Honduras": "HND", "Croatia": "HRV", "Haiti": "HTI", "Hungary": "HUN",
    "Indonesia": "IDN", "India": "IND", "Ireland": "IRL", "Iran, Islamic Rep.": "IRN", "Iraq": "IRQ",
    "Iceland": "ISL", "Israel": "ISR", "Italy": "ITA", "Jamaica": "JAM", "Jordan": "JOR",
    "Japan": "JPN", "Kazakhstan": "KAZ", "Kenya": "KEN", "Kyrgyz Republic": "KGZ", "Cambodia": "KHM",
    "Kiribati": "KIR", "Korea, Rep.": "KOR", "Kuwait": "KWT", "Lao PDR": "LAO", "Lebanon": "LBN",
    "Liberia": "LBR", "Libya": "LBY", "Saint Lucia": "LCA", "Liechtenstein": "LIE", "Sri Lanka": "LKA",
    "Lesotho": "LSO", "Lithuania": "LTU", "Luxembourg": "LUX", "Latvia": "LVA", "Macao SAR, China": "MAC",
    "Morocco": "MAR", "Monaco": "MCO", "Moldova": "MDA", "Madagascar": "MDG", "Maldives": "MDV",
    "Mexico": "MEX", "Marshall Islands": "MHL", "Macedonia, FYR": "MKD", "Mali": "MLI", "Malta": "MLT",
    "Myanmar": "MMR", "Montenegro": "MNE", "Mongolia": "MNG", "Mozambique": "MOZ", "Mauritania": "MRT",
        "Mauritius": "MUS", "Malawi": "MWI", "Malaysia": "MYS", "Namibia": "NAM", "New Caledonia": "NCL",
    "Niger": "NER", "Nigeria": "NGA", "Nicaragua": "NIC", "Netherlands": "NLD", "Norway": "NOR",
    "Nepal": "NPL", "New Zealand": "NZL", "Oman": "OMN", "Pakistan": "PAK", "Panama": "PAN",
    "Peru": "PER", "Philippines": "PHL", "Papua New Guinea": "PNG", "Poland": "POL", "Puerto Rico": "PRI",
    "Portugal": "PRT", "Paraguay": "PRY", "Qatar": "QAT", "Romania": "ROU", "Russia": "RUS",
    "Rwanda": "RWA", "Saudi Arabia": "SAU", "Sudan": "SDN", "Senegal": "SEN", "Singapore": "SGP",
    "Solomon Islands": "SLB", "Sierra Leone": "SLE", "El Salvador": "SLV", "Somalia": "SOM",
    "Serbia": "SRB", "South Sudan": "SSD", "Sao Tome and Principe": "STP", "Suriname": "SUR",
    "Slovak Republic": "SVK", "Slovenia": "SVN", "Sweden": "SWE", "Swaziland": "SWZ", "Seychelles": "SYC",
    "Chad": "TCD", "Togo": "TGO", "Thailand": "THA", "Tajikistan": "TJK", "Turkmenistan": "TKM",
    "Timor-Leste": "TLS", "Tonga": "TON", "Trinidad and Tobago": "TTO", "Tunisia": "TUN",
    "Turkey": "TUR", "Tuvalu": "TUV", "Tanzania": "TZA", "Uganda": "UGA", "Ukraine": "UKR",
    "Uruguay": "URY", "United States": "USA", "Uzbekistan": "UZB", "St. Vincent and the Grenadines": "VCT",
    "Venezuela, RB": "VEN", "Vietnam": "VNM", "Vanuatu": "VUT", "Samoa": "WSM", "Kosovo": "XKX",
    "Yemen, Rep.": "YEM", "South Africa": "ZAF", "Zambia": "ZMB", "Zimbabwe": "ZWE"
}

residential_dict = {
    "World": "XW", "OECD Total": "4T", "Austria": "AT", "Belgium": "BE", "Bulgaria": "BG",
    "Canada": "CA", "Chile": "CL", "Colombia": "CO", "Croatia": "HR", "Cyprus": "CY",
    "Czech Republic": "CZ", "Denmark": "DK", "Estonia": "EE", "Finland": "FI", "France": "FR",
    "Germany": "DE", "Greece": "GR", "Hungary": "HU", "Iceland": "IS", "India": "IN",
    "Ireland": "IE", "Israel": "IL", "Italy": "IT", "Japan": "JP", "Latvia": "LV",
    "Lithuania": "LT", "Luxembourg": "LU", "Malta": "MT", "Mexico": "MX", "Netherlands": "NL",
    "New Zealand": "NZ", "Norway": "NO", "Poland": "PL", "Portugal": "PT", "Romania": "RO",
    "Slovak Republic": "SK", "Slovenia": "SI", "South Africa": "ZA", "South Korea": "KR",
    "Spain": "ES", "Sweden": "SE", "Switzerland": "CH", "Turkey": "TR", "United Kingdom": "GB",
    "United States": "US", "North Macedonia": "MK", "Singapore": "SG", "Taiwan": "TW"
}

fred_interest_rate_codes = {
    "United States": "FEDFUNDS",            # Federal Funds Effective Rate
    "Canada": "INTGSTCANM193N",             # Bank of Canada Overnight Rate
    "Euro Area": "IRSTCI01EZM156N",         # Euro Area Short-Term Interest Rate
    "United Kingdom": "IRSTCI01GBM156N",    # UK Short-Term Interest Rate
    "Japan": "IRSTCI01JPM156N",             # Japan Short-Term Interest Rate
    "Australia": "IRSTCI01AUM156N",         # Australia Short-Term Interest Rate
    "Switzerland": "IRSTCI01CHM156N",       # Switzerland Short-Term Interest Rate
    "Norway": "IRSTCI01NOM156N",            # Norway Short-Term Interest Rate
    "Sweden": "IRSTCI01SEM156N",            # Sweden Short-Term Interest Rate
    "New Zealand": "IRSTCI01NZM156N",       # New Zealand Short-Term Interest Rate
    "South Korea": "IRSTCI01KRM156N",       # South Korea Short-Term Interest Rate
    "Brazil": "INTGSTBRM193N",               # Brazil Overnight Rate
    "Mexico": "INTGSTMXM193N",               # Mexico Overnight Rate
    "Russia": "INTGSTRUM193N",               # Russia Overnight Rate
}
month_dict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
