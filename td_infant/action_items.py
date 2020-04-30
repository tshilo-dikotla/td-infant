from edc_action_item import Action, site_action_items, HIGH_PRIORITY

INFANT_COVID_SCREENING_ACTION = 'update-infant-covid-results'


class InfantCovidScreeningAction(Action):
    name = INFANT_COVID_SCREENING_ACTION
    display_name = 'Update Infant Covid Screening Test Results'
    reference_model = 'td_infant.infantcovidscreening'
    admin_site_name = 'td_infant_admin'
    priority = HIGH_PRIORITY
    singleton = True

    def close_action_item_on_save(self):
        """Returns True if action item for \'action_identifier\'
        is to be closed on post_save.
        """
        return self.reference_model_obj.covid_results != 'pending'


site_action_items.register(InfantCovidScreeningAction)
