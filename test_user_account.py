#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Tests.
#
# The Initial Developer of the Original Code is Mozilla Foundation.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Bebe
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****



from unittestzero import Assert
import home_page
import addons_user_page

class TestUserAccounts:
    
    def test_user_login(self, testsetup):
        home= home_page.HomePage(testsetup)
        home.go_to_home_page()
        credentials = home.credentials_of_user('default')

        Assert.false(home.header.is_user_logged_in)
        

        home.header.click_login()
        addons_login_page = addons_user_page.AddonsLoginPage(testsetup)

        addons_login_page.login(credentials['email'], credentials['password'])
        Assert.true(home.header.is_user_logged_in)
	    def test_user_login(self, testsetup):
        home= home_page.HomePage(testsetup)
        home.go_to_home_page()
        credentials = home.credentials_of_user('default')

        Assert.false(home.header.is_user_logged_in)
        

        home.header.click_login()
        addons_login_page = addons_user_page.AddonsLoginPage(testsetup)

        addons_login_page.login(credentials['email'], credentials['password'])
        Assert.true(home.header.is_user_logged_in)
  teststsd
<<<<<<< HEAD
  gfjfgjf
=======
  
>>>>>>> origin/master
  
  test 3 
