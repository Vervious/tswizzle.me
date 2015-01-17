//
//  ViewController.swift
//  T-Swizzle
//
//  Created by Benjamin Y Chan on 1/17/15.
//  Copyright (c) 2015 tswizzle. All rights reserved.
//

import UIKit

class ViewController: UIViewController, FBLoginViewDelegate {
    
    
    @IBOutlet weak var fbLoginButton: UIButton!
    
    @IBAction func loginButtonTouchHandler(sender: AnyObject) {
        
        var permissions = ["public_profile", "email", "user_friends"]
        
        PFFacebookUtils.logInWithPermissions(permissions, {
            (user: PFUser!, error: NSError!) -> Void in
            if user == nil {
                NSLog("Uh oh. The user cancelled the Facebook login.")
                
            } else if user.isNew {
                NSLog("User signed up and logged in through Facebook!")
                self.performSegueWithIdentifier("toTheSwizzle", sender: self)
                
                
            } else {
                NSLog("User logged in through Facebook!")
                self.performSegueWithIdentifier("toTheSwizzle", sender: self)

            }
        })
        
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()

    }
    
    //FACEBOOK DELEGATE METHODS
    
    //If the user is already logged in
    
    func loginViewShowingLoggedInUser(loginView : FBLoginView!) {
        NSLog("User Logged In")
        
        self.performSegueWithIdentifier("toTheSwizzle", sender: self)
        
    }
    
    func loginViewFetchedUserInfo(loginView : FBLoginView!, user: FBGraphUser){
        NSLog("User Name: \(user.name)")
        
        var parseUser = PFUser()
        parseUser.username = user.name
        parseUser["phone"] = "123456789"
        
        parseUser.signUpInBackgroundWithBlock {
            (succeeded: Bool!, error: NSError!) -> Void in
            if error == nil {
                // Hooray! Let them use the app now.
            } else {
                NSLog("Error")
//                let errorString = error.userInfo["error"] as NSString
                // Show the errorString somewhere and let the user try again.
            }
        }
        
        
    }
    
    //If the user is logged out
    
    func loginViewShowingLoggedOutUser(loginView : FBLoginView!) {
        NSLog("User Logged Out")
    }
    
    //Errors
    
    func loginView(loginView : FBLoginView!, handleError:NSError) {
        NSLog("Error: \(handleError.localizedDescription)")
    }
    
    

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

