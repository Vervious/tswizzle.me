//
//  ViewController.swift
//  T-Swizzle
//
//  Created by Benjamin Y Chan on 1/17/15.
//  Copyright (c) 2015 tswizzle. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.logInWithFacebook()
        
    }
    
    func logInWithFacebook() {
        
//        PFFacebookUtils.logInWithPermissions(permissions, {
//            (user: PFUser!, error: NSError!) -> Void in
//            if user == nil {
//                NSLog("Uh oh. The user cancelled the Facebook login.")
//            } else if user.isNew {
//                NSLog("User signed up and logged in through Facebook!")
//            } else {
//                NSLog("User logged in through Facebook!")
//            }
//        })

}

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

