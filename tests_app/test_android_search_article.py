from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_open_article():
    with step('Type search article "Kitimat"'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Kitimat')

    with step('Open article'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).click()

    with step('Verify of checked article'):
        browser.element((AppiumBy.ID, 'pcs-edit-section-title-description')).\
            should(have.text('District municipality in British Columbia, Canada'))


# index	1
# package	org.wikipedia.alpha
# class	android.widget.TextView
# text	Capital and largest city of Russia
# resource-id	pcs-edit-section-title-description

# package	org.wikipedia.alpha
# class	android.widget.TextView
# text	District municipality in British Columbia, Canada
# resource-id	pcs-edit-section-title-description

#
# index	0
# package	org.wikipedia.alpha
# class	android.widget.TextView
# text	Kitimat
#
#
# index	1
# package	org.wikipedia.alpha
# class	android.widget.TextView
# text	District municipality in British Columbia, Canada
# resource-id	pcs-edit-section-title-description
# checkable	false
#
#
#
# index	2
# package	org.wikipedia.alpha
# class	android.view.View
# text
# resource-id	pcs-edit-section-divider
# checkable	false
# checked	false
#
#
# index	1
# package	org.wikipedia.alpha
# class	android.view.View
# text
# checkable	false
# checked	false
#
#
# index	1
# package	org.wikipedia.alpha
# class	android.widget.LinearLayout
# text
# resource-id	org.wikipedia.alpha:id/page_header_view
# checkable	false

