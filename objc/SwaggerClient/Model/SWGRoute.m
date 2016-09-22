#import "SWGRoute.h"

@implementation SWGRoute

- (instancetype)init {
  self = [super init];
  if (self) {
    // initialize property's default value, if any
    
  }
  return self;
}


/**
 * Maps json key to property name.
 * This method is used by `JSONModel`.
 */
+ (JSONKeyMapper *)keyMapper {
  return [[JSONKeyMapper alloc] initWithDictionary:@{ @"vehicle_id": @"vehicleId", @"distance": @"distance", @"transport_time": @"transportTime", @"completion_time": @"completionTime", @"waiting_time": @"waitingTime", @"activities": @"activities" }];
}

/**
 * Indicates whether the property with the given name is optional.
 * If `propertyName` is optional, then return `YES`, otherwise return `NO`.
 * This method is used by `JSONModel`.
 */
+ (BOOL)propertyIsOptional:(NSString *)propertyName {

  NSArray *optionalProperties = @[@"vehicleId", @"distance", @"transportTime", @"completionTime", @"waitingTime", @"activities"];
  return [optionalProperties containsObject:propertyName];
}

@end
