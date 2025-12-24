from rules.models import Rule, RuleExecution


def matches_condition(transaction, conditions):
    description = transaction.description.lower()

    keywords = conditions.get("description_contains", [])
    min_amount = conditions.get("min_amount")
    max_amount = conditions.get("max_amount")

    if keywords:
        if not any(word.lower() in description for word in keywords):
            return False

    if min_amount is not None and transaction.amount > max_amount:
        return False

    if max_amount is not None and transaction.amount > max_amount:
        return False

    return True


def apply_rules(transaction):
    rules = Rule.objects.filter(user=transaction.user, is_active=True).order_by(
        "priority"
    )

    for rule in rules:
        if matches_condition(transaction, rule.conditions):
            transaction.category = rule.category
            transaction.save(update_fields=["category"])

        RuleExecution.objects.create(rule=rule, transaction=transaction)
        break
