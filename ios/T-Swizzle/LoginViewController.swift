//
//  ViewController.swift
//  T-Swizzle
//
//  Created by Benjamin Y Chan on 1/17/15.
//  Copyright (c) 2015 tswizzle. All rights reserved.
//

import UIKit

class ViewController: UIViewController, FBLoginViewDelegate {
    
    @IBOutlet var fbLoginView : FBLoginView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.fbLoginView.delegate = self;
        self.fbLoginView.readPermissions = ["public_profile", "email", "user_friends"]

    }
    
    //FACEBOOK DELEGATE METHODS
    
    //If the user is already logged in
    
    func loginViewShowingLoggedInUser(loginView : FBLoginView!) {
        NSLog("User Logged In")
        
        self.performSegueWithIdentifier("toTheSwizzle", sender: self)
        
    }
    
    func loginViewFetchedUserInfo(loginView : FBLoginView!, user: FBGraphUser){
        NSLog("User Name: \(user.name)")
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

