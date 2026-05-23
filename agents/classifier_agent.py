def classify_issue(issue):

    issue_lower = issue.lower()

    # CATEGORY + TEAM
    if any(word in issue_lower for word in [

        "wifi",
        "vpn",
        "network",
        "internet",
        "connection"
    ]):

        category = "Network"

        team = "Network Support"

    elif any(word in issue_lower for word in [

        "email",
        "outlook",
        "mail"
    ]):

        category = "Email"

        team = "Messaging Team"

    elif any(word in issue_lower for word in [

        "system",
        "software",
        "application",
        "update",
        "app",
        "crash"
    ]):

        category = "Software"

        team = "Application Support"

    elif any(word in issue_lower for word in [

        "password",
        "authentication",
        "login",
        "account"
    ]):

        category = "Access Issue"

        team = "Identity Support"

    else:

        category = "General"

        team = "IT Helpdesk"

    # PRIORITY
    if any(word in issue_lower for word in [

        "urgent",
        "critical",
        "failed",
        "down",
        "immediately",
        "crashing"
    ]):

        priority = "High"

    else:

        priority = "Medium"

    return {

        "category": category,

        "priority": priority,

        "team": team
    }