//
//  SwizzleViewController.swift
//  T-Swizzle
//
//  Created by Benjamin Y Chan on 1/17/15.
//  Copyright (c) 2015 tswizzle. All rights reserved.
//

import UIKit

class SwizzleViewController: UIViewController, UITextViewDelegate, FBRequestConnectionDelegate {
    
    @IBOutlet weak var inputTextView: UITextView!
    @IBOutlet weak var sendButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        if(FBSession.activeSession().isOpen) {
            NSLog("FBSession is active")
            
        
        }
    }
    
    

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func textViewShouldEndEditing(textView: UITextView) -> Bool {
        
        return true
    }
    
    
    @IBAction func makeSwizzle(sender: UIButton) {
        
        //call the API --> get an mp4 video
        //post the mp4 to Facebook with a call to Graph API
        
        self.uploadToFacebook()

        
//        var params = Dictionary <String, NSObject>()

        
    }
    
    func uploadToFacebook() {
        
        if (FBSession.activeSession().isOpen){
            
        
        var videoData = NSData.initialize()
        var params = ["videoData": "videoData", "contentType": "video/quicktime", "title": "Title", "description": "This video was made by Tswizzle.me"]
            
        
            FBRequestConnection.startWithGraphPath("me/videos", parameters: params, HTTPMethod: "POST") { (FBRequestConnection connection, AnyObject object, NSError error) -> Void in
                
                NSLog("Uploaded video to Facebook!")
                
            }
            

        }   
        
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
